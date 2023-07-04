from django.urls import path
from . import views

urlpatterns = [
    path('ag/', views.AddGrocery, name='addgrocery_url'),
    path('sg/', views.ShowGrocery, name='showgrocery_url')
]