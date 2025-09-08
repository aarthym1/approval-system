from django.shortcuts import render

def home(request):
    return render(request, 'student/home.html')

def submit_project(request):
    return render(request, 'student/submit_project.html')

def project_status(request):
    return render(request, 'student/project_status.html')

def profile(request):
    return render(request, 'student/profile.html')

def profile(request):
    return render(request, "student/profile.html")