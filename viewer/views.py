from django.shortcuts import render

from .models import TagsModel, ClipsModel


# Get the list of video project
def video_clips(request):
    clips = ClipsModel.objects.all()
    return render(request, "clip_temp/video_clips.html", {"clips": clips})


def video_clip_detail(request, video_name):
    return render(request, "clip_temp/video_clip_detail.html")
