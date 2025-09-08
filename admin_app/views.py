from django.shortcuts import render

def home(request):
    return render(request, 'admin_app/home.html')

def manage_users(request):
    return render(request, 'admin_app/manage_users.html')

def projects_overview(request):
    return render(request, 'admin_app/projects_overview.html')

def settings(request):
    return render(request, 'admin_app/settings.html')




