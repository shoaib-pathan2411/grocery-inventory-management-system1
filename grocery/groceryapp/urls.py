from django.urls import path
from . import views

urlpatterns = [
    path('addgrocery/', views.AddGrocery, name='addgrocery_url'),
    path('showgrocery/', views.ShowGrocery, name='showgrocery_url')
]