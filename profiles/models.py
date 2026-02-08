from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    education = models.CharField(max_length=255, blank=True)
    bio = models.TextField(blank=True)

    skills = models.ManyToManyField(Skill, related_name="profiles", blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="projects"
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    tech_stack = models.ManyToManyField(Skill, related_name="projects", blank=True)

    github_link = models.URLField(blank=True)
    live_link = models.URLField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
