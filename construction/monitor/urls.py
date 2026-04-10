from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('project/', views.project),
    path('worker/', views.worker),
    path('material/', views.material),
    path('budget/', views.budget),
    path('dashboard/', views.dashboard),
]