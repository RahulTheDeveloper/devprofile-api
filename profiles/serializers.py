from rest_framework import serializers
from .models import Profile, Project, Skill


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ["id", "name"]



class ProjectSerializer(serializers.ModelSerializer):
    tech_stack = serializers.PrimaryKeyRelatedField(
        queryset=Skill.objects.all(),
        many=True,
        required=False
    )

    class Meta:
        model = Project
        fields = [
            "id",
            "profile",      
            "title",
            "description",
            "tech_stack",
            "github_link",
            "live_link",
            "created_at",
        ]


class ProfileSerializer(serializers.ModelSerializer):
     skills = serializers.PrimaryKeyRelatedField(
        queryset=Skill.objects.all(),
        many=True,
        required=False
    )
    #  skills_detail = SkillSerializer(source="skills", many=True, read_only=True)
    
     projects = ProjectSerializer(many=True, read_only=True)

     class Meta:
        model = Profile
        fields = [
            "id",
            "name",
            "email",
            "education",
            "bio",
            "skills",
            "projects",
            "created_at",
        ]
