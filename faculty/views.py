from django.shortcuts import render

def home(request):
    return render(request, 'faculty/home.html')

def guidelines(request):
    return render(request, 'faculty/guidelines.html')

def project_review(request):
    return render(request, 'faculty/project_review.html')

def dashboard(request):
    return render(request, 'faculty/dashboard.html')



