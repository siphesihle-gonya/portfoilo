from django.urls import path
from . import views
from .views import ProjectListAPI
from rest_framework.routers import DefaultRouter


urlpatterns = [

    path("api/projects/", views.ProjectListAPI.as_view(), name="projects_api"),
    path("api/projects/<int:pk>/redirect/", views.project_redirect_view, name="project_redirect"),

]
