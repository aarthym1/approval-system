# faculty_app/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'faculty/home.html')


