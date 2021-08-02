from django.urls import path
from blog.views import *

urlpatterns = [
    path('<str:id>',detail, name="detail"),
    path('new/', new, name="new"),
    path('create/', create, name="create"),
    path('edit/<str:id>', edit, name="edit"), #detail페이지로 연결
    path('update/<str:id>',update, name="update"),
    path('delete/<str:id>',delete, name="delete"),
]