from django.urls import path

from main.views import show_main, create_project, show_experience, create_experience, show_achievement, create_achievement

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("project/add", create_project, name="create_project"),
    path("experience/", show_experience, name="show_experience"),
    path("experience/add/", create_experience, name="create_experience"),
    path("achievement/", show_achievement, name="show_achievement"),
    path("achievement/add/", create_achievement, name="create_achievement"),
]   