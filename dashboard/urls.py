from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='dashboard-index'),
    path('transport/', views.transportPage, name='dashboard-transport'),
    path('mechanical/', views.mechanicalPage, name='dashboard-mechanical'),
    path('electrical/', views.electricalPage, name='dashboard-electrical'),

]
