from django.shortcuts import render, redirect
from .models import Service, Appointment

def home(request):
    services = Service.objects.all()
    bookings = Appointment.objects.all().order_by("-id")
    return render(request, "home.html", {
        "services": services,
        "bookings": bookings
    })

def services(request):
    services = Service.objects.all()
    return render(request, "services.html", {"services": services})


def booking(request):   
    services = Service.objects.all()

    if request.method == "POST":
        Appointment.objects.create(
            name=request.POST["name"],
            phone=request.POST["phone"],
            service_id=request.POST["service"],
            date=request.POST["date"],
            time=request.POST["time"]
        )
        return redirect("/")

    return render(request, "booking.html", {"services": services})

def contact(request):
    return render(request, "contact.html")
