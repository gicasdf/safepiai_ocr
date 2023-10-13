import os
from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse, HttpResponse

from .ai_helper import load_ai_model, predict_with_model

from .forms import ImageDataForm
from . models import ImageData

#이미지 제공을 위한 코드
def get_image(request, image_name):
    image_path = os.path.join(settings.BASE_DIR, 'ocrmodel', 'images', image_name)
    with open(image_path, 'rb') as f:
        return HttpResponse(f.read(), content_type='image/png')

#모델 이미지 결과값 반환 api
def ai_model(image_path):
    result_path = 'path_to_processed_image.jpg'
    return result_path

def api_view(request):
    if request.method =='POST':
        form = ImageDataForm(request.POST, request.FILES)
        if form.is_valid():
            image_data = form.cleaned_data['image']
            image_instance = ImageData.objects.create(image=image_data)
            image_path = os.path.join(settings.MEDIA_ROOT, str(image_instance.image))
            result_path = ai_model(image_path)

            #처리된 이미지 경로 반환
            return JsonResponse({'result_path': result_path})
    else:
        form = ImageDataForm()

    return render(request, 'api.html', {'form': form})

#모델 로드 도우미 모듈 함수
def ocr_three(request):
    model = load_ai_model()

    input_data = os.path.join(settings.MEDIA_ROOT)
    result = predict_with_model(model, input_data)
