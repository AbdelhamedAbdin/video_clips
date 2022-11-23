from django.db import models
from django.core.validators import FileExtensionValidator


def create_course(self, filename):
    return f"{self.course.category.name}/{self.course.name}/{filename}"


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Course(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default="")
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ClipsModel(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="course")
    video = models.FileField(null=False,
                             validators=[
                                 FileExtensionValidator(
                                     allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])
                                 ],
                             upload_to=create_course
                             )
    viewed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ('-video',)
