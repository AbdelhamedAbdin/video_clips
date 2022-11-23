# Django Apps
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
# Apps
from .models import ClipsModel, Course
from viewer.pagers import page_navigation


def filter_videos(tag_list_request: list) -> ClipsModel.objects.all():
    # Videos Query-sets
    queryset = ClipsModel.objects.all()

    if tag_list_request:
        queryset = queryset.filter(course__name__in=tag_list_request)

    return queryset


# Get the list of video project
def video_clips(request):
    tags = Course.objects.all()
    choices_list = request.GET.getlist("choices")
    videos = filter_videos(choices_list)
    paginator = Paginator(videos, 48)
    page_number = request.GET.get('page')
    get_page = paginator.get_page(page_number)
    pager = page_navigation(get_page, page_number)

    context = {
        "tags": tags,
        "choices": choices_list,
        'next_url': pager['next_url'],
        'prev_url': pager['prev_url'],
        'videos': get_page,
        'is_pager': pager['is_pager']
    }
    return render(request, "clip_temp/video_clips.html", context)


def video_clip_detail(request, video_id=None):
    video = get_object_or_404(ClipsModel, id=video_id)
    video.viewed = True
    video.save()
    return render(request, "clip_temp/video_clip_detail.html", {'video': video})
