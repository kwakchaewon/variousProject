from django import forms
from .models import Blog


# 블로그 생성
class CreateBlog (forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'body', 'author']
