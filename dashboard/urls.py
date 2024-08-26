from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.index, name='dashboard-index'),
    path('dashboard/issue', views.issuePage, name='dashboard-issue'),
   
]
