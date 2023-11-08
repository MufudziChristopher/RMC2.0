from django.urls import path

from . import views

app_name = "RMC2_0"


urlpatterns = [
    #Leave as empty string for base url
	path('', views.RMC, name="RMC2_0"),
    ]
