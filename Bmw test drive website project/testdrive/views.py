from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Vehicle, TestDriveBooking as Booking, Profile
from .forms import TestDriveBookingForm, SignUpForm


def home(request):
    return render(request, "testdrive/home.html")


def vehicles(request):
    all_vehicles = Vehicle.objects.all()
    return render(request, "testdrive/vehicles.html", {"vehicles": all_vehicles})


def register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user, date_of_birth=form.cleaned_data["date_of_birth"])
            login(request, user)
            return redirect("vehicles")
    else:
        form = SignUpForm()
    return render(request, "testdrive/register.html", {"form": form})


@login_required(login_url='login')
def book_test_drive(request):
    if request.method == "POST":
        form = TestDriveBookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect("booking_success")
    else:
        form = TestDriveBookingForm()
        form.fields['email'].initial = request.user.email
        vehicle_id = request.GET.get('vehicle')
        if vehicle_id:
            vehicle = get_object_or_404(Vehicle, pk=vehicle_id)
            form.fields['vehicle'].initial = vehicle
    return render(request, "testdrive/book_test_drive.html", {"form": form})


@login_required(login_url='login')
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, "testdrive/my_bookings.html", {"bookings": bookings})


def booking_success(request):
    return render(request, "testdrive/booking_success.html")