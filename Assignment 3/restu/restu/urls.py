from django.contrib import admin
from django.urls import path, include
from . import views
from meal.views import meal 
from about_us.views import about_us
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="base"),
    path('meal/', include("meal.urls")),
    path('about_us/', include("about_us.urls")),
    path('show_meals/', meal, name="meal"),
    path('about_us/', about_us, name="about_us"),
]
