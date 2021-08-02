from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="list"),
    path('delete/<str:id>/', views.deleteTask, name="delete"),
    path('edit/<str:id>', views.editTask, name="edit"),
    path('update/<str:id>', views.updateTask, name="update"),
]