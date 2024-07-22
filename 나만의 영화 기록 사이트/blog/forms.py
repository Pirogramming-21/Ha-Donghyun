from django import forms

from .models import Post
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = (
            "title",
            "released_date",
            "genre",
            "rating",
            "running_time",
            "text",
            "movieauthor",
            "actor",
        )
        labels = {
            "title": "제목",
            "released_date": "개봉년도",
            "genre": "장르",
            "rating": "별점",
            "running_time": "러닝타임",
            "text": "리뷰",
            "movieauthor": "감독",
            "actor": "배우",
        }


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            "username",
            "password",
        )
        labels = {
            "username": "아이디",
            "password": "비밀번호",
        }
