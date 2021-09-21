from django.db import models

class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
    type_choices = [
        ('pianocovers', 'Piano cover'),
        ('guitarcovers', 'Guitar cover'),
        ('projects', 'Coding project'),
    ]
    type = models.CharField(
        max_length=50,
        choices=type_choices,
        default='pianocover'
    )

    def __str__(self):
        return self.summary
