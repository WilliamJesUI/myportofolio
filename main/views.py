from django.shortcuts import render

from main.models import Experience


def show_main(request):
    context = {
        "name": "William Jesiel",
        "npm": "2506637155",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "A Computer Science student at the University of Indonesia. Ready to overcome every obstacle cuz I got that dawg in me!  "
            "Hover over me to see the dawg in me!"
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "William Jesiel",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)