from django import template

register = template.Library()


@register.simple_tag
def video_name(value):
    # extensions = ['MOV', 'avi', 'mp4', 'webm', 'mkv']
    split_path = value.split("/")
    return split_path[-1]
