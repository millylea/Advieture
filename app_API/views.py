from django.shortcuts import render
from django.http import JsonResponse
from app_travel.models import Tour

# Create your views here.
def domestic_tours(request):
    tours = Tour.objects.all()
    list_tours = list(tours.values())
    return JsonResponse(list_tours, safe=False)