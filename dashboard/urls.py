from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='dashboard-index'),
    path('project/', views.projectPage, name='dashboard-project'),
    path('civil/', views.transportPage, name='dashboard-civil'),
    path('mechanical/', views.mechanicalPage, name='dashboard-mechanical'),
    path('electrical/', views.electricalPage, name='dashboard-electrical'),

]
