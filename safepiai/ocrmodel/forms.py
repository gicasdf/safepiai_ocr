from django import forms

#양식 생성
class ImageDataForm(forms.Form):
    image = forms.ImageField()