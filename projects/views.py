from django.shortcuts import render, get_object_or_404

from .models import Project

def projects(request):
    projects = Project.objects
    return render(request, 'projects/projects.html', {'projects':projects})
