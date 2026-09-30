from django.shortcuts import render

from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.http import require_POST
from django.core.exceptions import PermissionDenied
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from main.models import *
from main.forms import *

import datetime


def show_main(request):
    last_login = request.COOKIES.get('last_login', 'No active login session / Cookie not found')
    context = {
        "name": "William Jesiel",
        "npm": "2506637155",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "A Computer Science student at the University of Indonesia. Ready to overcome every obstacle cuz I got that dawg in me!  "
            "Hover over me to see the dawg in me!"
        ),
        "last_login" : last_login,
        "project_list": Project.objects.all(),
    }
    return render(request, "index.html", context)

@login_required(login_url="/login/")
def create_project(request):
    if not request.user.is_superuser:
        raise PermissionDenied
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


def get_experiences_json(request):
    title_query = request.GET.get("title", "").strip()
    experiences = Experience.objects.prefetch_related('starred_by').all()

    if title_query:
        experiences = experiences.filter(title__icontains=title_query)

    # Manually build the JSON data so we can add the Star logic
    data = []
    for experience in experiences:
        starred_users = experience.starred_by.all()
        is_starred = request.user in starred_users if request.user.is_authenticated else False
        starred_by_names = ", ".join([u.username for u in starred_users])

        data.append({
            "pk" : str(experience.id),
            "fields" : {
                "title": experience.title,
                "description": experience.description,
                "category": experience.category,
                "star_count": starred_users.count(),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
            }
        })

    return JsonResponse(data, safe=False)

def show_experience(request):
    title_query = request.GET.get("title", "").strip()
    context = {
        "name": "William Jesiel",
        "title_query": title_query,
        "form": ExperienceForm(),
    }
    return render(request, "experience.html", context)

@login_required(login_url="/login/")
def create_experience(request):
    if not request.user.is_superuser:
        raise PermissionDenied

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

@login_required(login_url="/login/")
@permission_required('main.change_experience', raise_exception=True)
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

@login_required(login_url="/login/")
def delete_experience(request, experience_id):
    if not request.user.is_superuser:
        raise PermissionDenied
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

@login_required(login_url="/login/")
def create_achievement(request):
    if not request.user.is_superuser:
        raise PermissionDenied


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

@login_required(login_url="/login/")
@permission_required('main.change_achievement', raise_exception=True)
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
    name_query = request.GET.get("name", "" ).strip()
    achievements = Achievement.objects.all()

    if name_query:
        achievements = achievements.filter(name__icontains=name_query)

    achievements_json = serializers.serialize("json", achievements, use_natural_foreign_keys=True)
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

@login_required(login_url="/login/")
def delete_achievement(request, achievement_id):
    if not request.user.is_superuser:
        raise PermissionError

    achievement = get_object_or_404(Achievement, pk=achievement_id)

    if request.method == "POST":
        achievement.delete()
        messages.success(request, "Achievement deleted!")
        return redirect("main:show_achievement")

    return redirect("main:show_achievement")

def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Account created successfully. Please log in.")
        return redirect("main:login")

    context = {
        "name" : "William",
        "form" : form,
    }

    return render(request, "register.html", context)

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        login(request, form.get_user())
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "name" : "William",
        "form" : form,
    }
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response

@login_required(login_url="/login/")
def toggle_star(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        if request.user in experience.starred_by.all():
            experience.starred_by.remove(request.user)
        else:
            experience.starred_by.add(request.user)
    return redirect("main:show_experience")

@login_required(login_url="/login/")
def toggle_flame(request, achievement_id):
    achievement = get_object_or_404(Achievement, pk=achievement_id)

    if request.method == "POST":
        if request.user in achievement.flamed_by.all():
            achievement.flamed_by.remove(request.user)
        else:
            achievement.flamed_by.add(request.user)
    return redirect("main:show_achievement")

@require_POST
def create_experience_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Only the portfolio owner can add experiences."},
            status=403,
        )

    form = ExperienceForm(request.POST)
    if form.is_valid():
        experience = form.save()
        return JsonResponse(
            {"message": "Experience added successfully.", "pk": str(experience.id)},
            status=201,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)



