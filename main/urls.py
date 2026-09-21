from django.urls import path

from main.views import *

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("project/add/", create_project, name="create_project"),
    path("experience/", show_experience, name="show_experience"),
    path("experience/add/", create_experience, name="create_experience"),
    path("experience/<uuid:experience_id>/update/", update_experience, name="update_experience"),
    path("experiences/<uuid:experience_id>/delete/", delete_experience, name="delete_experience"),
    path("api/experiences/", get_experiences_json, name="get_experiences_json"),
    path("achievement/", show_achievement, name="show_achievement"),
    path("achievement/add/", create_achievement, name="create_achievement"),
    path("achievement/<uuid:achievement_id>/update/", update_achievement, name="update_achievement"),
    path("achievements/<uuid:achievement_id>/delete/", delete_achievement, name="delete_achievement"),
    path("api/achievements/", get_achievements_json, name="get_achievements_json"),
]   