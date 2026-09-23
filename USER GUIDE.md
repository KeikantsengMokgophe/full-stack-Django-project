# BMW Test Drive Website
## User Guide

### 1. Introduction

Welcome to the BMW Test Drive Website User Guide.

This guide explains how users can navigate the website, browse available BMW vehicles, view vehicle information, and book a test drive.

The website was developed as a full-stack Django project designed to provide a simple and professional way for users to explore BMW vehicles and request a test drive.

### 2. Purpose of the Website

The purpose of the BMW Test Drive Website is to give car enthusiasts an easy way to explore available BMW vehicles and request a test drive.

The website allows users to:

- Browse the available BMW vehicles.
- View information about each vehicle.
- Select a vehicle they are interested in.
- Complete a test drive booking form.
- Submit their booking request through the website.

The website focuses on making the test drive booking process simple, clear, and easy to navigate.

### 3. How to Access the Website

To access the BMW Test Drive Website while running the project locally:

1. Open the project in **Visual Studio Code**.
2. Open the terminal in Visual Studio Code.
3. Navigate to the project folder.
4. Start the Django development server using:

```bash
py manage.py runserver
```

5. Open a web browser such as Google Chrome.
6. Enter the local website address:

`http://127.0.0.1:8000/`

7. The BMW Test Drive Website home page will appear.

**Note:** The Django server must be running in the terminal for the website to be accessible.

### 4. Home Page

The Home Page is the first page users see when they open the BMW Test Drive Website.

The page provides an overview of the website and allows users to navigate to the main sections of the website.

The Home Page includes:

- A professional navigation bar.
- BMW branding and website information.
- A section introducing the test drive experience.
- A call-to-action that allows users to explore the available vehicles.
- Navigation links that help users move around the website.

Users can use the navigation bar to access the different sections of the website and begin the process of selecting a BMW vehicle for a test drive.

### 5. Browsing BMW Vehicles

Users can browse the BMW vehicles available on the website before making a test drive booking.

To browse the vehicles:

1. Use the navigation bar to open the **Vehicles** section.
2. View the BMW vehicles displayed on the page.
3. Each vehicle is presented with an image and basic information.
4. Select a vehicle to view more information about it.
5. If the user is interested in the vehicle, they can proceed to the **Book a Test Drive** option.

This allows users to compare the available vehicles and choose the BMW they would like to test drive.

### 6. Viewing Vehicle Details

Users can view additional information about a BMW vehicle before deciding to book a test drive.

To view the vehicle details:

1. Go to the **Vehicles** section.
2. Select the BMW vehicle you are interested in.
3. View the vehicle's image and available information.
4. Review the details to decide whether the vehicle is suitable for a test drive.
5. Select **Book a Test Drive** when ready to continue.

The vehicle details page helps users make an informed choice before submitting a test drive booking.

### 7. Booking a Test Drive

Users can request a test drive for the BMW vehicle they have selected.

To book a test drive:

1. Select **Book a Test Drive** for the chosen vehicle.
2. The booking page will open.
3. Enter the required personal and contact information.
4. Select the preferred date and time for the test drive.
5. Check that all the information entered is correct.
6. Submit the booking form.

After submitting the form, the booking information will be processed by the website.

Users should make sure that the information they provide is accurate so that they can be contacted regarding their test drive request.

### 8. Completing the Booking Form

The booking form collects the information needed to process a user's test drive request.

Users should complete all required fields on the form.

The information may include:

- **Full Name** – The user's first and last name.
- **Email Address** – An email address that can be used for communication.
- **Phone Number** – A contact number for the test drive request.
- **Preferred Date** – The date the user would like to have the test drive.
- **Preferred Time** – The user's preferred time for the test drive.
- **Selected Vehicle** – The BMW vehicle the user wants to test drive.

Before submitting the form, users should check that all information is correct.

After completing the form, select the **Submit Booking** button to send the test drive request.

### 9. Booking Confirmation

After the user submits the test drive booking form, the website processes the booking information.

The user should receive confirmation that the booking request has been submitted successfully.

The confirmation allows the user to know that their test drive request has been received.

Users should keep their booking information available in case they need to refer to their test drive request later.

### 10. Admin/Management Features

The website includes Django administration features that can be used to manage information stored by the website.

An authorised administrator can use the admin area to manage:

- BMW vehicle information.
- Test drive bookings.
- User information related to bookings.
- Booking dates and times.

To access the Django admin area:

1. Start the Django development server.
2. Open the website in a browser.
3. Go to the Django admin page.
4. Log in using the administrator account.
5. Select the relevant section to view or manage the available information.

The admin area is intended for authorised users who are responsible for managing the website's information and test drive requests.

### 11. Troubleshooting

If the website does not work as expected, users can check the following common issues.

**Website does not open**

- Make sure the Django development server is running.
- Check that the correct local address is being used.
- Confirm that there are no errors displayed in the terminal.

**Images are not displaying**

- Check that the image file is stored in the correct folder.
- Confirm that the image path in the HTML template is correct.
- Make sure Django static files are configured correctly.

**Booking form does not submit**

- Check that all required fields have been completed.
- Make sure the information entered is valid.
- Check the terminal for Django error messages.

**Changes are not appearing on the website**

- Save the files in Visual Studio Code.
- Refresh the browser.
- If necessary, restart the Django development server.

If the problem continues, check the Django terminal output for error messages that may help identify the issue.

### 12. Conclusion

The BMW Test Drive Website provides users with a simple and convenient way to explore BMW vehicles and request a test drive.

By following this user guide, users can navigate the website, view available vehicles, review vehicle information, complete a booking form, and submit a test drive request.

The guide also provides basic troubleshooting steps to help users resolve common problems when using the website.

The website was developed using Django to provide a structured and functional platform for managing vehicles and test drive bookings.
