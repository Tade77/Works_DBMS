from django.shortcuts import render
# from django.http import HttpResponse 
# Create your views here.

def index(request):
    return render(request, "dashboard_template/index.html")
def projectPage(request):
    return render(request, "dashboard_template/project.html")


def transportPage(request):
    return render(request, "dashboard_template/civil.html")

def mechanicalPage(request):
    return render(request, "dashboard_template/mechanical.html")
def electricalPage(request):
    return render(request, "dashboard_template/electrical.html")