from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("profile/", views.profile, name="profile"),
    path("", views.home, name="student_home"),
    path("submit/", views.submit_project, name="submit_project"),
    path("status/", views.project_status, name="project_status"),
]

