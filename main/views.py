from django.shortcuts import render

from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from main.models import Achievement
from main.models import Experience
from main.models import Project

from main.forms import ExperienceForm


def show_main(request):
    context = {
        "name": "William Jesiel",
        "npm": "2506637155",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "A Computer Science student at the University of Indonesia. Ready to overcome every obstacle cuz I got that dawg in me!  "
            "Hover over me to see the dawg in me!"
        ),
        "project_list": Project.objects.all(),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "William Jesiel",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def create_experience(request):
    form = ExperienceForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Successfully added new experience!!")
        return redirect("main:show_experience")

    context = {
        "name": "William",
        "form": form,
    }
    return render(request, "projects_form.html", context)


def show_achievement(request):
    context = {
        "name": "William Jesiel",
        "achievement_list": Achievement.objects.all(),
    }
    return render(request, "achievement.html", context)