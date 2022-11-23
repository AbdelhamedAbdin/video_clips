from . import views

from django.urls import path

app_name = "viewer"

urlpatterns = [
    path("", views.video_clips, name="video_clips"),
    path("video/<int:video_id>/", views.video_clip_detail, name="video_target")
]
