from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils import timezone
from .models import TestDriveBooking


class TestDriveBookingForm(forms.ModelForm):

    class Meta:
        model = TestDriveBooking
        fields = [
            "vehicle",
            "full_name",
            "email",
            "phone",
            "date",
            "time",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["date"].input_formats = ["%Y-%m-%d"]
        self.fields["date"].widget = forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"})

        self.fields["time"].widget = forms.TimeInput(format="%H:%M", attrs={"type": "time"})

    def clean_date(self):
        date = self.cleaned_data["date"]
        if date < timezone.localdate():
            raise forms.ValidationError("Please choose today or a future date.")
        return date

    def clean(self):
        cleaned_data = super().clean()

        vehicle = cleaned_data.get("vehicle")
        date = cleaned_data.get("date")
        time = cleaned_data.get("time")

        if vehicle and date and time:
            existing_booking = TestDriveBooking.objects.filter(
                vehicle=vehicle,
                date=date,
                time=time
            ).exists()

            if existing_booking:
                raise forms.ValidationError(
                    "This vehicle is already booked for that date and time. "
                    "Please choose another time."
                )

        return cleaned_data


class SignUpForm(UserCreationForm):
    date_of_birth = forms.DateField(
        widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
        input_formats=["%Y-%m-%d"],
        label="Date of Birth",
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "date_of_birth"]

    def clean_date_of_birth(self):
        dob = self.cleaned_data["date_of_birth"]
        today = timezone.localdate()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

        if age < 18:
            raise forms.ValidationError("You must be at least 18 years old to create an account.")

        return dob