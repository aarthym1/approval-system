from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="faculty_home"),
    path("guidelines/", views.guidelines, name="guidelines"),
    path("review/", views.project_review, name="project_review"),
    path("dashboard/", views.dashboard, name="faculty_dashboard"),
]
