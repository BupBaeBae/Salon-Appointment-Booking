# Nail Salon Appointment Scheduler

This is a Django-based web application that allows a nail salon to manage and schedule appointments for multiple artists (e.g., Ngoc and Hong) offering manicure and pedicure services. The application allows clients to view available slots, book appointments, and cancel using a unique key.

## Problem Formulation

Nail salons often rely on pen-and-paper scheduling or generic booking tools that are not tailored for their specific service durations, time slot structures, or staff availability. This project seeks to create a simple, web-based system where clients can book and cancel appointments, and the salon can manage available slots per artist and service type.

## Original Notebook

The project was originally developed as a Python notebook that implemented the appointment scheduling logic for a nail salon. This notebook served as the foundation for building the Django web application. The transition from notebook to web app involved converting the logic into Django models, forms, views, and templates to create a fully functional website.

## Features

- View available appointment slots by artist and time
- Support for multiple services: manicure and pedicure
- Booking with guest name and slot selection
- Cancellation using a unique key
- Preload command to initialize artists and time slots

## Technologies Used

- Django (Python)
- SQLite (default database)
- HTML templates for views

## Setup Instructions

0. Download and unzip the project archive:

   Download the file named `NgocNguyen_INST126_SP_25.zip`, then extract it to a working folder using your file manager or by right-clicking and choosing "Extract All...".

1. Clone the repository:

   ```bash
   git clone https://github.com/BupBaeBae/Salon-Appointment-Booking.git
   cd Salon-Appointment-Booking
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install django
   ```

4. Run initial migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Preload data:

   ```bash
   python manage.py preload_data
   ```

6. Start the server:

   ```bash
   python manage.py runserver
   ```

7. Open your browser and visit:
   [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Demo Requirements

- The project includes a custom Django management command to preload two artists (Ngoc and Hong) with manicure and pedicure slots.
- Functionality is demonstrated via a working booking and cancellation system.

## Author

- GitHub: [BupBaeBae](https://github.com/BupBaeBae) (Ngoc Nguyen)

## License

This project is for academic purposes only.
