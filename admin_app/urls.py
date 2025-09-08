from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="admin_home"),
    path("manage-users/", views.manage_users, name="manage_users"),
    path("projects-overview/", views.projects_overview, name="projects_overview"),
    path("settings/", views.settings, name="admin_settings"),
]
