from django.shortcuts import render
from .models import Project

# Create your views here.
def portfolio_home(request):
    projects = Project.objects.all().order_by('-created_at')
    return render(request, 'portfolio/home.html', {'projects': projects})