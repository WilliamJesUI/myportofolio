from django.forms import ModelForm, TextInput, Textarea, MultipleChoiceField
from django.forms.widgets import CheckboxSelectMultiple

from main.models import Achievement, Experience, Project

class AchievementForm(ModelForm):
    class Meta:
        model = Achievement
        fields = [
            "name",
            "description",
            "thumbnail"
        ]

        labels = {
            "name": "Achievement Name",
            "description": "Achievement Description",
            "thumbnail": "Achievement Thumbnail"
        }

        widgets = {
            "name": TextInput(
                attrs={
                    "placeholder": "Hackathon",
                    "maxlength": 255,
                }
            ),

            "description": Textarea(
                attrs={
                    "placeholder": "Tell us about your achievement",
                    "rows": 3
                }
            ),

            "thumbnail": TextInput(
                attrs={
                    "placeholder": "Put a link to your image"
                }
            ),
        }



class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = [
            "title",
            "description",
            "category",
        ]

        labels = {
            "title": "Experience Title",
            "description": "Experience Description",
            "category": "Experience Category",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Teaching Assistant",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Tell us about your experience",
                    "rows": 3,
                }
            ),
            "category":TextInput(
                attrs={
                    "placeholder": "Full-time",
                    "maxlength": 255,
                }
            ),
        }

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "name",
            "description",
            "thumbnail",
            "download_url",
        ]

        labels = {
            "name": "Project Name",
            "description": "Project Description",
            "thumbnail": "Project Thumbnail",
            "download_url": "Project Download Url",
        }

        widgets = {
            "name": TextInput(
                attrs={
                    "placeholder": "Your project name",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Describe your project",
                    "rows": 3,
                }
            ),
            "thumbnail":TextInput(
                attrs={
                    "placeholder": "URL to your project thumbnail",
                    "maxlength": 255,
                }
            ),
            "download_url":TextInput(
                attrs={
                    "placeholder": "URL to download your project"
                }
            )
        }