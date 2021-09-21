from django.shortcuts import render, get_object_or_404

from .models import Job

def home(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs':jobs})

def decideredirect(request, job_id):
    job  = get_object_or_404(Job, pk=job_id)
    type = job.type
    return type
