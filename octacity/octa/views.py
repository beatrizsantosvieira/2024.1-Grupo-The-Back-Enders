from django.shortcuts import render
import cv2
from django.http import StreamingHttpResponse
from django.views.decorators import gzip

#o gzip ajuda na compactação dos dados, resumindo, fica mais rapido pra transferir

@gzip.gzip_page
def camera_stream(request):
    cap = cv2.VideoCapture(0)  #0 para a primeira câmera disponível

#essa função pega os frames da camera e transforma em jpg
    def generate_frames():
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            _, buffer = cv2.imencode('.jpg', frame)
            frame_bytes = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

            #encerre o loop se a tecla 'q' é apertada
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    return StreamingHttpResponse(generate_frames(), content_type='multipart/x-mixed-replace; boundary=frame')
