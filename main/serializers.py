from django.utils.html import strip_tags
from rest_framework import serializers

from main.models import Achievement, Experience, Project

class ExperienceSerializer(serializers.ModelSerializer):
    star_count = serializers.SerializerMethodField()
    is_starred = serializers.SerializerMethodField()
    starred_by_names = serializers.SerializerMethodField()

    class Meta:
        model = Experience
        fields = [
            "id", "title", "description", "category",
            "star_count", "is_starred", "starred_by_names",
            ]
        read_only_fields = ["id"]

    def validate_title(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError("Title cannot be empty.")
        return value

    def validate_description(self, value):
        return strip_tags(value)

    def validate_category(self, value):
        return strip_tags(value)

    def get_star_count(self, obj):
        return obj.starred_by.count()

    def get_is_starred(self, obj):
        request = self.context.get("request")
        if request is None or not request.user.is_authenticated:
            return False
        return request.user in obj.starred_by.all()

    def get_starred_by_names(self, obj):
        return ", ".join(user.username for user in obj.starred_by.all())

class AchievementSerializer(serializers.ModelSerializer):
    flame_count = serializers.SerializerMethodField()
    is_flamed = serializers.SerializerMethodField()
    flamed_by_names = serializers.SerializerMethodField()

    class Meta:
        model = Achievement
        fields = [
            "id", "name", "description", "thumbnail",
            "flame_count", "is_flamed", "flamed_by_names",
        ]

    def validate_name(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError("Name cannot be empty.")
        return value

    def validate_description(self, value):
        return strip_tags(value)

    def validate_thumbnail(self, value):
        return strip_tags(value)

    def get_flame_count(self, obj):
        return obj.flamed_by.count()

    def get_is_flamed(self, obj):
        request = self.context.get("request")
        if (request is None or not request.user.is_authenticated):
            return False
        return request.user in obj.flamed_by.all()

    def get_flamed_by_names(self, obj):
        return ", ".join(user.username for user in obj.flamed_by.all())

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
            model = Achievement
            fields = [
                "id", "name", "description", "thumbnail", "download_url"
            ]
    
    def validate_name(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError("Name cannot be empty.")
        return value

    def validate_description(self, value):
        return strip_tags(value)

    def validate_thumbnail(self, value):
        return strip_tags(value)

    def validate_download_url(self, value):
        return strip_tags(value)
