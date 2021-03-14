from django.contrib import admin 
from django.urls import path 

# importing views from views..py 
from .views import dashboard

urlpatterns = [ 
	path('dashboard/', dashboard, name='dashboard' ), 
] 
