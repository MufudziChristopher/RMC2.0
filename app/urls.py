from django.urls import path

from . import views

app_name = "app"


urlpatterns = [
    #Leave as empty string for base url
	path('', views.app, name="app"),
    ]