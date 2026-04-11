from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('project/', views.project, name='project'),
    path('worker/', views.worker, name='worker'),
    path('material/', views.material, name='material'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('edit/<int:id>/', views.edit_project, name='edit_project'),
    path('delete-material/<int:id>/', views.delete_material, name='delete_material'),
    path('delete/<int:id>/', views.delete_project, name='delete_project'),
    path('delete-worker/<int:id>/', views.delete_worker, name='delete_worker'),
    path('budget/', views.budget, name='budget'),
    path('delete-budget/<int:id>/', views.delete_budget, name='delete_budget'),
    path('reset-budget/', views.reset_budget, name='reset_budget'),
]