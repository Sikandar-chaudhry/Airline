from django.shortcuts import render
from .models import Flight,Passenger
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.


def index (request):
    return render (request , "flights/index.html",{
        "flights" : Flight.objects.all()
    })
    
    
def flight(request , flight_id):
    
    # pk instead of id , stands for primary key
    flight = Flight.objects.get(id=flight_id)
    return render(request, "flights/flight.html", {
        "flight" : flight,
        "passengers" : flight.passengers.all(),
        "non_passengers" : Passenger.objects.exclude(flights =flight).all()
    })
    
def book (request , flight_id):
    if request.method == "POST":
        # Accessing the flight
        flight = Flight.objects.get(pk=flight_id)

        # Finding the passenger id from the submitted form data
        passenger_id = int(request.POST["passenger"])

        # Finding the passenger based on the id
        passenger = Passenger.objects.get(pk=passenger_id)

        # Add passenger to the flight
        passenger.flights.add(flight)
        
        return HttpResponseRedirect(reverse("flight:flight" ,args = (flight.id,)))