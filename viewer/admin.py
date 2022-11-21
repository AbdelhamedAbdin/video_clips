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

    # def save_model(self, request, obj, form, change):
    #
    #     category = ClipsModel.objects.get(id=int(request.POST['category']))
    #     try:
    #         album = request.POST['album']
    #     except:
    #         album = ""
    #
    #     try:
    #         if album != "":
    #             album_name = Album.objects.filter(category__id=category.id).get(id=int(album))
    #         else:
    #             album_name = None
    #     except Album.DoesNotExist:
    #         raise ValidationError(
    #             "يوجد خطا فى العلاقة بين الالبوم والفئة التى تم اختيارها من فضلك تاكد من الاسم واعد المحاولة")
    #
    #     for data in request.FILES.getlist('images'):
    #         Gallery.objects.create(images=data, category=category, album=album_name)


admin.site.register(TagsModel)
admin.site.register(ClipsModel)
