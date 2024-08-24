from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse 
# Create your views here.
@login_required(login_url='user-login')
def index(request):
    return render(request, "dashboard_template/index.html")
@login_required(login_url='user-login')
def projectPage(request):
    return render(request, "dashboard_template/project.html")

@login_required(login_url='user-login')
def transportPage(request):
    return render(request, "dashboard_template/civil.html")
@login_required(login_url='user-login')
def mechanicalPage(request):
    return render(request, "dashboard_template/mechanical.html")
@login_required(login_url='user-login')
def electricalPage(request):
    return render(request, "dashboard_template/electrical.html")