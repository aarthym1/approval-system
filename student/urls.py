from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='student-home'),  # home page of student app
]
