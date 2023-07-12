from django.shortcuts import render
from .models import Flight
from django.shortcuts import get_object_or_404
# Create your views here.


def index (request):
    return render (request , "flights/index.html",{
        "flights" : Flight.objects.all()
    })
    
    
def flight(request , flight_id):
    
    # pk instead of id , stands for primary key
    flight = Flight.objects.get(id=flight_id)
    return render(request, "flights/flight.html", {
        "flight" : flight
    })