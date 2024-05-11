from django.shortcuts import render, redirect, get_object_or_404
from .models import Camera
from .forms import CameraForm
import cv2
from django.http import StreamingHttpResponse
from django.views.decorators import gzip

def camera_list(request):
    cameras = Camera.objects.all()
    return render(request, 'cameras/camera_list.html', {'cameras': cameras})

def camera_detail(request, pk):
    camera = Camera.objects.get(pk=pk)
    return render(request, 'cameras/camera_detail.html', {'camera': camera})

def camera_create(request):
    if request.method == 'POST':
        form = CameraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('camera_list')
    else:
        form = CameraForm()
    return render(request, 'cameras/camera_form.html', {'form': form})

def camera_update(request, pk):
    camera = get_object_or_404(Camera, pk=pk)
    if request.method == 'POST':
        form = CameraForm(request.POST, instance=camera)
        if form.is_valid():
            form.save()
            return redirect('camera_detail', pk=pk)
    else:
        form = CameraForm(instance=camera)
    return render(request, 'cameras/camera_form.html', {'form': form})

def camera_delete(request, pk):
    camera = get_object_or_404(Camera, pk=pk)
    if request.method == 'POST':
        camera.delete()
        return redirect('camera_list')
    return render(request, 'cameras/camera_confirm_delete.html', {'camera': camera})

@gzip.gzip_page
def video_feed(request, pk):
     # Obtém o objeto Camera com base no ID fornecido
    camera = get_object_or_404(Camera, pk=pk)

    # Endereço IP e porta da câmera
    camera_ip = camera.ip_address
    camera_port = camera.port

    # URL do fluxo de vídeo da câmera IP
    video_url = f'http://{camera_ip}:{camera_port}/video'

    # Inicializa o objeto VideoCapture com a URL do fluxo de vídeo
    cap = cv2.VideoCapture(video_url)

    # Função para gerar frames do fluxo de vídeo
    def frame_generator():
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            # Convertendo o frame em bytes
            _, buffer = cv2.imencode('.jpg', frame)
            frame_bytes = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

    # Retorna a resposta HTTP com a transmissão de vídeo
    return StreamingHttpResponse(frame_generator(), content_type='multipart/x-mixed-replace; boundary=frame')