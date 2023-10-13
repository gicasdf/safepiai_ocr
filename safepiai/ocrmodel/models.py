from django.db import models


#모델 생성
class ImageData(models.Model):
    image = models.ImageField(upload_to='images/')
