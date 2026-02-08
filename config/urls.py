
from django.contrib import admin
from django.urls import path,include
from profiles.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('profiles.urls')),
    path("", home),
]
