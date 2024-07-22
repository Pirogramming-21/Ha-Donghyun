from django.urls import path
from . import views

app_name = "insta"

urlpatterns = [
  path("", views.main, name="main"),
  path('insta/create/', views.insta_create, name='create'),
  path("insta/likes/<int:pk>", views.likes, name="likes"),
  path("insta/comment/<int:pk>", views.comment, name="comment"),
  path("insta/comment/<int:pk>/create", views.comment_create, name="comment_create"),
  path("insta/comment/<int:pk>/delete", views.comment_delete, name="comment_delete"),
  path("signup/", views.signup, name="signup"),
  path("login/", views.login, name="login"),
  path("logout/", views.logout, name="logout"),
]
