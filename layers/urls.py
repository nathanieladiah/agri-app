from django.urls import path

from . import views

urlpatterns = [
	path('', views.layer_home, name='layer_home'),
]