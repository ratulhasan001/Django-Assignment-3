from django.urls import path
from . import views
urlpatterns = [
    path('', views.meal),
    path('index/',views.index, name="index")
]
