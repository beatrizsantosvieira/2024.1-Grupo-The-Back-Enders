from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Company, CameraPark, Camera
from .forms import CompanyForm, CameraParkForm, CameraForm
import cv2
from django.http import StreamingHttpResponse
from django.views.decorators import gzip
import urllib.parse

def company_list(request):
    companies = Company.objects.all()
    return render(request, 'companies/company_list.html', {'companies': companies})

def company_detail(request, pk):
    company = get_object_or_404(Company, pk=pk)
    return render(request, 'companies/company_detail.html', {'company': company})

def company_create(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('company_list')
    else:
        form = CompanyForm()
    return render(request, 'companies/company_form.html', {'form': form})

def company_update(request, pk):
    company = get_object_or_404(Company, pk=pk)
    if request.method == 'POST':
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            return redirect('company_detail', pk=company.pk)
    else:
        form = CompanyForm(instance=company)
    return render(request, 'companies/company_form.html', {'form': form})

def company_delete(request, pk):
    company = get_object_or_404(Company, pk=pk)
    if request.method == 'POST':
        company.delete()
        return redirect('company_list')
    return render(request, 'companies/company_confirm_delete.html', {'company': company})

def camera_park_detail(request, pk):
    camera_park = get_object_or_404(CameraPark, pk=pk)
    company = camera_park.company
    return render(request, 'camera_parks/camera_park_detail.html', {'camera_park': camera_park, 'company': company})

def camera_park_create(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    if request.method == "POST":
        form = CameraParkForm(request.POST)
        if form.is_valid():
            camera_park = form.save(commit=False)
            camera_park.company = company
            camera_park.save()
            return redirect('camera_park_detail', pk=camera_park.pk)
    else:
        form = CameraParkForm(initial={'company': company})
    return render(request, 'camera_parks/camera_park_form.html', {'form': form, 'company': company})

def camera_park_update(request, pk):
    camera_park = get_object_or_404(CameraPark, pk=pk)
    company = camera_park.company
    if request.method == "POST":
        form = CameraParkForm(request.POST, instance=camera_park)
        if form.is_valid():
            form.save()
            return redirect('camera_park_detail', pk=camera_park.pk)
    else:
        form = CameraParkForm(instance=camera_park)
    return render(request, 'camera_parks/camera_park_form.html', {'form': form, 'camera_park': camera_park, 'company': company})

def camera_park_delete(request, pk):
    camera_park = get_object_or_404(CameraPark, pk=pk)
    if request.method == "POST":
        camera_park.delete()
        return redirect('company_detail', pk=camera_park.company.pk)
    return render(request, 'camera_parks/camera_park_confirm_delete.html', {'camera_park': camera_park})

def camera_detail(request, pk):
    camera = get_object_or_404(Camera, pk=pk)
    camera_park = camera.camera_park
    return render(request, 'cameras/camera_detail.html', {'camera': camera, 'camera_park' : camera_park})

def camera_create(request, camera_park_id):
    camera_park = get_object_or_404(CameraPark, pk=camera_park_id)
    if request.method == "POST":
        form = CameraForm(request.POST)
        if form.is_valid():
            camera = form.save(commit=False)
            camera.camera_park = camera_park
            camera.save()
            return redirect('camera_detail', pk=camera.pk)
    else:
        form = CameraForm(initial={'camera_park': camera_park})
    return render(request, 'cameras/camera_form.html', {'form': form, 'camera_park': camera_park})

def camera_update(request, pk):
    camera = get_object_or_404(Camera, pk=pk)
    camera_park = camera.camera_park
    if request.method == 'POST':
        form = CameraForm(request.POST, instance=camera)
        if form.is_valid():
            form.save()
            return redirect('camera_detail',  pk=camera.pk)
    else:
        form = CameraForm(instance=camera)
    return render(request, 'cameras/camera_form.html', {'form': form, 'camera_park': camera_park})

def camera_delete(request, pk):
    camera = get_object_or_404(Camera, pk=pk)
    if request.method == 'POST':
        camera.delete()
        return redirect('camera_park_detail', pk=camera.camera_park.pk)
    return render(request, 'cameras/camera_confirm_delete.html', {'camera': camera})

@gzip.gzip_page
def video_feed(request, pk):
    # Obtém o objeto Camera com base no ID fornecido
    camera = get_object_or_404(Camera, pk=pk)

    # Endereço IP e porta da câmera
    protocol = camera.network_stream_protocol.lower()
    camera_ip = camera.ip_address
    camera_port = camera.port
    username = urllib.parse.quote(camera.username)
    password = urllib.parse.quote(camera.password)

    # URL do fluxo de vídeo da câmera IP
    match protocol:
        case 'rtsp':
            video_url = f'rtsp://{username}:{password}@{camera_ip}:{camera_port}/stream'
        case 'http':
            video_url = f'http://{username}:{password}@{camera_ip}:{camera_port}/video'
        case 'https':
            video_url = f'https://{username}:{password}@{camera_ip}:{camera_port}/video'
        case _:
            raise ValueError(f"Unsupported protocol: {protocol}")

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