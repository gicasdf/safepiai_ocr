from django.urls import path
from .views import api_view, get_image

#패턴 정의
urlpatterns = [
    #이미지 받는 패턴 정의
    path('images/<str:image_name>/', get_image, name='get_image'),
    path('api/', api_view, name='api'),
]