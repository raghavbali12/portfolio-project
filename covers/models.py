from django.db import models
from django.core.validators import FileExtensionValidator

class Cover(models.Model):
    title = models.CharField(max_length=200)
    type_choices = [
        ('pianocovers', 'Piano'),
        ('guitarcovers', 'Guitar'),
    ]
    cover_type = models.CharField(
        max_length=50,
        choices=type_choices,
        default='None'
    )
    thumbnail = models.ImageField(upload_to='images/')
    performance  = models.FileField(upload_to='videos/',null=True,
validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    summary = models.TextField()

    def __str__(self):
        return self.title
