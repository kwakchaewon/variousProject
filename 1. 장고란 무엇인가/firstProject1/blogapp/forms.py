from django import forms
from .models import Blog
from ckeditor_uploader.widgets import CKEditorUploadingWidget

# 블로그 생성
class CreateBlog (forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'body', 'author']
        widgets = {
            'title': forms.TextInput(
                attrs={'class' : 'form-control', 'style': 'width:100%','placeholder':'제목을 입력하세요.'}
            ),
            'author': forms.Select(
                attrs={'class' : 'custom-select'}
            ),
            'body': forms.CharField(widget=CKEditorUploadingWidget()),
        }
