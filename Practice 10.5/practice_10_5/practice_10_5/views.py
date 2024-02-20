from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def home(request):
    d = { 'adding' : 5, 'lst' : [1, 2, 4], 'tme' : datetime.datetime.now(), 'meals': [
        {
            "strMeal": "BeaverTails",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/ryppsv1511815505.jpg",
            "idMeal": "52928"
        },
        {
            "strMeal": "Breakfast Potatoes",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/1550441882.jpg",
            "idMeal": "52965"
        },
        {
            "strMeal": "Canadian Butter Tarts",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/wpputp1511812960.jpg",
            "idMeal": "52923"
        }
    ]}
    return render(request, 'index.html', d)

def contact(request):
    return render(request, 'firstapp/contact.html')
def about(request):
    return render(request, 'firstapp/about.html')