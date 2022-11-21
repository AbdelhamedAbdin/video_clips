from django.db import models
from django.core.validators import FileExtensionValidator


class TagsModel(models.Model):
    tag = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.tag


class ClipsModel(models.Model):
    tag = models.ManyToManyField(TagsModel, related_name="tags", default="")
    video = models.FileField(null=False, validators=[
                                 FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
    viewed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)
