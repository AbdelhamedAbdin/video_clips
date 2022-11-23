from django.contrib import admin
from .models import *


class MultipleVideoManaged(admin.ModelAdmin):
    list_display = ('id', 'video')

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj=None, **kwargs)
        form.base_fields['video'].widget.attrs = {
            'multiple': 'multiple'
        }
        return form

    def save_model(self, request, obj, form, change):
        course = Course.objects.get(id=int(request.POST['course']))

        for data in request.FILES.getlist('video'):
            ClipsModel.objects.create(video=data, course=course)


admin.site.register(ClipsModel, MultipleVideoManaged)
admin.site.register(Category)
admin.site.register(Course)

