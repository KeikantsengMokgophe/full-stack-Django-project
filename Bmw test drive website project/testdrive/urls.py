from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("vehicles/", views.vehicles, name="vehicles"),
    path("register/", views.register, name="register"),
    path("book-test-drive/", views.book_test_drive, name="book_test_drive"),
    path("my-bookings/", views.my_bookings, name="my_bookings"),
    path("booking-success/", views.booking_success, name="booking_success"),
    path('accounts/', include('django.contrib.auth.urls')),
]
