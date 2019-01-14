from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string

from .models import Job
from .forms import JobForm


def job_list(request):
    jobs = Job.objects.all()
    return render(request, "jobs/job_list.html", {"jobs": jobs})


def save_job_form(request, form, template_name):
    data = dict()
    if request.method == "POST":
        if form.is_valid():
            form.save()
            data["form_is_valid"] = True
            jobs = Job.objects.all()
            data["html_job_list"] = render_to_string(
                "jobs/includes/partial_job_list.html", {"jobs": jobs}
            )
        else:
            data["form_is_valid"] = False
    context = {"form": form}
    data["html_form"] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def job_create(request):
    if request.method == "POST":
        form = JobForm(request.POST)
    else:
        form = JobForm()
    return save_job_form(request, form, "jobs/includes/partial_job_create.html")


def job_update(request, pk):
    job = get_object_or_404(Job, pk=pk)
    if request.method == "POST":
        form = JobForm(request.POST, instance=job)
    else:
        form = JobForm(instance=job)
    return save_job_form(request, form, "jobs/includes/partial_job_update.html")


def job_delete(request, pk):
    job = get_object_or_404(Job, pk=pk)
    data = dict()
    if request.method == "POST":
        job.delete()
        data["form_is_valid"] = True
        jobs = Job.objects.all()
        data["html_job_list"] = render_to_string(
            "jobs/includes/partial_job_list.html", {"jobs": jobs}
        )
    else:
        context = {"job": job}
        data["html_form"] = render_to_string(
            "jobs/includes/partial_job_delete.html", context, request=request
        )
    return JsonResponse(data)
