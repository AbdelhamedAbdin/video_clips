from . import views

from django.urls import path

app_name = "clip_view"

urlpatterns = [
    path("", views.video_clips, name="video_clips")
]
