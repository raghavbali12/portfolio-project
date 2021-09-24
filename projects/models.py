from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    file  = models.FileField(upload_to='files/',null=True)
    description = models.TextField()

    def __str__(self):
        return self.title
