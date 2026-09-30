from django.forms import ModelForm, TextInput, Textarea, MultipleChoiceField
from django.forms.widgets import CheckboxSelectMultiple
from django.core.exceptions import ValidationError
from django.utils.html import strip_tags

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

    def clean_title(self):
        title = strip_tags(self.cleaned_data["title"]).strip()
        if not title:
            raise ValidationError("Experience name can't contain only HTML tags.")
        return title

    def clean_description(self):
        return strip_tags(self.cleaned_data["description"]).strip()

    def clean_category(self):
        return strip_tags(self.cleaned_data["category"]).strip()

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