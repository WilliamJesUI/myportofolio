from django.shortcuts import render

from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from main.models import Achievement
from main.models import Experience
from main.models import Project

from main.forms import AchievementForm, ExperienceForm, ProjectForm


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

def create_project(request):
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Successfully added a new project!!")
        return redirect("main:show_main")

    context = {
        "name": "William",
        "form": form,
    }
    return render(request, "project_form.html", context)

def update_project(request):
    pass

def get_experiences_json(request):
    title_query = request.GET.get("title", "").strip()
    experiences = Experience.objects.all()

    if title_query:
        experiences = experiences.filter(title__icontains=title_query)

    experiences_json = serializers.serialize("json", experiences)
    return HttpResponse(experiences_json, content_type="application/json")

def show_experience(request):
    title_query = request.GET.get("title", "").strip()
    experience_list = Experience.objects.all()
    if title_query:
        experience_list = experience_list.filter(title__icontains=title_query)

    context = {
        "name": "William Jesiel",
        "experience_list": experience_list,
        "title_query": title_query,
    }

    return render(request, "experience.html", context)

def create_experience(request):
    form = ExperienceForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Successfully added a new experience!!")
        return redirect("main:show_experience")

    context = {
        "name": "William",
        "form": form,
    }
    return render(request, "experience_form.html", context)

def update_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)
    form = ExperienceForm(request.POST or None, instance=experience)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("main:show_experience")
    else:
        form = ExperienceForm(instance=experience)

    context = {
        "name": "William",
        "form": form,
        "experience": experience
    }
    return render(request, "experience_update.html", context)


def delete_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        experience.delete()
        messages.success(request, "Experience deleted!")
        return redirect("main:show_experience")

    return redirect("main:show_experience")


def show_achievement(request):
    name_query = request.GET.get("name", "").strip()
    achievement_list = Achievement.objects.all()

    if name_query:
        achievement_list = achievement_list.filter(name__icontains=name_query)

    context = {
        "name": "William Jesiel",
        "achievement_list": achievement_list,
        "name_query": name_query,
    }
    return render(request, "achievement.html", context)

def create_achievement(request):
    form = AchievementForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Successfully added a new achievement!!")
        return redirect("main:show_achievement")

    context = {
        "name": "William",
        "form": form
    }
    return render(request, "achievement_form.html", context)



def update_achievement(request, achievement_id):
    achievement = get_object_or_404(Achievement, pk=achievement_id)
    form = AchievementForm(request.POST or None, instance=achievement)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("main:show_achievement")
    else:
        form = AchievementForm(instance=achievement)

    context = {
        "name": "William",
        "form": form,
        "achievement": achievement
    }

    return render(request, "achievement_update.html", context)

def get_achievements_json(request):
    name_query = request.GET.get("name", "").strip()
    achievements = Achievement.objects.all()

    if name_query:
        achievements = achievements.filter(name__icontains=name_query)

    achievements_json = serializers.serialize("json", achievements)
    return HttpResponse(achievements_json, content_type="application/json")

def show_achievements(request):
    json_response = get_achievements_json(request)

    achievements = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    achievements = [achievement.object for achievement in achievements]
    name_query = request.GET.get("name", "").strip()

    context = {
        "name": "William",
        "achievement_list": achievements,
        "name_query": name_query,
    }
    return render(request, "achievement.html", context)

def delete_achievement(request, achievement_id):
    achievement = get_object_or_404(Achievement, pk=achievement_id)

    if request.method == "POST":
        achievement.delete()
        messages.success(request, "Achievement deleted!")
        return redirect("main:show_achievement")

    return redirect("main:show_achievement")

