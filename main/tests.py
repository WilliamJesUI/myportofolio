from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from main.models import Achievement, Experience, Project


class MainTest(TestCase):
    def setUp(self):
        self.achievement = Achievement.objects.create(
            name="Hackathon",
            description="Created Chatgpt myself!",
            thumbnail="image.png",
        )

        self.experience = Experience.objects.create(
            title="IDS Teaching Assistant",
            description="Help students understand digital systems.",
            category="part-time",
        )

        self.project = Project.objects.create(
            name="Burhan Quest",
            description="I love Burhan",
            thumbnail="Burhan.png",
            download_url="www.burhan.com",

        )

    def test_main_url_is_accessible(self):
        response=self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.experience.title)
        self.assertNotContains(response, self.achievement.name)
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')
        self.assertContains(response, f'href="{reverse("main:show_achievement")}"')

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/a-page-that-does-not-exist/")

        self.assertEqual(response.status_code, 404)

    def test_project_model(self):
        self.assertEqual(str(self.project), "Burhan Quest")
        self.assertEqual(self.project.description, "I love Burhan")
        self.assertEqual(self.project.thumbnail, "Burhan.png")
        self.assertEqual(self.project.download_url, "www.burhan.com")

    def test_project_page(self):
        response = self.client.get(reverse("main:show_main"))
        self.assertContains(response, self.project.name)
        self.assertContains(response, self.project.description)

    def test_empty_project_page(self):
        Project.objects.all().delete()
        response = self.client.get(reverse("main:show_main"))

        self.assertContains(response, "No Project has been added yet!")

    def test_experience_model(self):
        self.assertEqual(str(self.experience), "IDS Teaching Assistant")
        self.assertEqual(self.experience.category, "part-time")
        self.assertTrue(self.experience.is_ongoing)

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, self.experience.title)
        self.assertContains(response, self.experience.description)
        self.assertContains(response, "Part-Time")
        self.assertContains(response, "Ongoing")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')


    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))

        self.assertContains(response, "No experience has been added yet.")

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()
        response = self.client.get(reverse("main:show_experience"))

        self.assertFalse(self.experience.is_ongoing)
        self.assertContains(response, "Completed")
        self.assertNotContains(response, "Ongoing")

    def test_achievement_model(self):
        self.assertEqual(str(self.achievement), "Hackathon")
        self.assertEqual(self.achievement.name, "Hackathon")
        self.assertEqual(self.achievement.description, "Created Chatgpt myself!")
        self.assertEqual(self.achievement.thumbnail, "image.png")

    def test_achievement_page(self):
        response = self.client.get(reverse("main:show_achievement"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "achievement.html")
        self.assertContains(response, self.achievement.name)
        self.assertContains(response, self.achievement.description)
        self.assertContains(response, f'href="{reverse("main:show_main")}"')
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')

    def test_empty_achievement_page(self):
        Achievement.objects.all().delete()
        response = self.client.get(reverse("main:show_achievement"))

        self.assertContains(response, "William is kinda achievementless rn...")

