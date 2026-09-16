from django.forms import ModelForm, TextInput, Textarea
from main.models import Experience

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = [
            "title",
            "description",
            "category",
        ]

        labels = {
            "title": "Experience title",
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
            "category": TextInput(
                attrs={
                    "placeholder": "Part-time, Full-time, Freelance",
                }
            ),
        }