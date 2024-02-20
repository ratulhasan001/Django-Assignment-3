from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mealapp/', include("mealapp.urls")),
    path('', views.home),
    path('index/', views.index)
]
