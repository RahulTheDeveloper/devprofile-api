from django.urls import path
from .views import (
    ProfileCreateAPIView,
    ProfileDetailAPIView,
    ProfileUpdateAPIView,
    ProjectBySkillAPIView,
    TopSkillsAPIView,
    SearchAPIView,
    HealthAPIView,
    SkillCreateAPIView, SkillListAPIView,ProjectCreateAPIView,ProjectListAPIView,home
)

urlpatterns = [
    path("health/", HealthAPIView.as_view()),
    path("skills/create/", SkillCreateAPIView.as_view()),
    path("skills/", SkillListAPIView.as_view()),
   
    path("profiles/", ProfileCreateAPIView.as_view()),
    path("profiles/<int:pk>/", ProfileDetailAPIView.as_view()),
    path("profiles/<int:pk>/update/", ProfileUpdateAPIView.as_view()),

    path("projects/create", ProjectCreateAPIView.as_view()),
    path("projects/", ProjectListAPIView.as_view()),

    path("projects/by-skill/", ProjectBySkillAPIView.as_view()),
    path("skills/top/", TopSkillsAPIView.as_view()),
    path("search/", SearchAPIView.as_view()),

]
