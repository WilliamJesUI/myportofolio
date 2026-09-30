import uuid

from django.db import models
from django.contrib.auth.models import User

class Achievement(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    flamed_by = models.ManyToManyField(User, related_name="flamed_achievements", blank=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    download_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class Experience(models.Model):
    EXPERIENCE_CHOICES = [
        ("internship", "Internship"),
        ("research", "Research"),
        ("volunteer", "Volunteer"),
        ("part-time", "Part-Time"),
        ("full-time", "Full-Time"),
        ("freelance", "Freelance"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(
        max_length=20,
        choices=EXPERIENCE_CHOICES,
        default="full-time",
    )
    starred_by = models.ManyToManyField(
        User, related_name="starred_experiences", blank=True
    )


    def __str__(self):
        return self.title

    @property
    def is_ongoing(self):
        return self.ended_at is None