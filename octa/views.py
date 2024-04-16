from django.shortcuts import render
import cv2
from django.http import StreamingHttpResponse
from django.views.decorators import gzip

@gzip.gzip_page
def camera_stream(request):
    cap = cv2.VideoCapture(0)  # 0 para a primeira câmera disponível

    def generate_frames():
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # Realize o processamento do frame, se necessário

            _, buffer = cv2.imencode('.jpg', frame)
            frame_bytes = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

            # Encerre o loop se a tecla 'q' for pressionada
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    return StreamingHttpResponse(generate_frames(), content_type='multipart/x-mixed-replace; boundary=frame')
