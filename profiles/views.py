from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Count, Q
from .models import Profile, Project, Skill
from .serializers import ProfileSerializer, ProjectSerializer, SkillSerializer
from django.shortcuts import render


class HealthAPIView(APIView):
    def get(self, request):
        return Response({"status": "ok"})
    

class SkillCreateAPIView(APIView):
    def post(self, request):
        serializer = SkillSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

class SkillListAPIView(APIView):
    def get(self, request):
        skills = Skill.objects.all().order_by("name")
        serializer = SkillSerializer(skills, many=True)
        return Response(serializer.data)

class ProfileCreateAPIView(APIView):
    def post(self, request):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            profile = Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            return Response({"error": "Profile not found"}, status=404)

        serializer = ProfileSerializer(profile)
        return Response(serializer.data)


class ProfileUpdateAPIView(APIView):
    def put(self, request, pk):
        try:
            profile = Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            return Response({"error": "Profile not found"}, status=404)

        serializer = ProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class ProjectCreateAPIView(APIView):
    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ProjectListAPIView(APIView):
    def get(self, request):
        projects = Project.objects.all().order_by("-created_at")
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)


class ProjectBySkillAPIView(APIView):
    def get(self, request):
        skill_name = request.query_params.get("skill")

        projects = Project.objects.all()

        if skill_name:
            projects = projects.filter(tech_stack__name__iexact=skill_name)

        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)


class TopSkillsAPIView(APIView):
    def get(self, request):
        skills = Skill.objects.annotate(total=Count("projects")).order_by("-total")[:5]
        serializer = SkillSerializer(skills, many=True)
        return Response(serializer.data)


class SearchAPIView(APIView):
    def get(self, request):
        query = request.query_params.get("q")

        profiles = Profile.objects.filter(
            Q(name__icontains=query) |
            Q(skills__name__icontains=query) |
            Q(projects__title__icontains=query)
        ).distinct()

        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)


def home(request):
    return render(request, "index.html")
