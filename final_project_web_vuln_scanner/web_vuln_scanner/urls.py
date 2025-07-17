from django.urls import path,include
from . import views
urlpatterns = [

    path('',views.index ),  # Include URLs from the web_vuln_scanner app
]
