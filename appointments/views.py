
from django.shortcuts import render, redirect
from .models import Slot, Guest
from .forms import BookingForm, CancelForm
import random

def home(request):
    slots = Slot.objects.filter(is_open=True).order_by('time')
    return render(request, 'appointments/home.html', {'slots': slots})

def book_appointment(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            slot = form.cleaned_data['slot']
            key = str(random.randint(1000, 9999))
            Guest.objects.create(name=name, appointment=slot, key=key)
            slot.is_open = False
            slot.guest_key = key
            slot.save()
            return render(request, 'appointments/confirmation.html', {'name': name, 'key': key})
    else:
        form = BookingForm()
    return render(request, 'appointments/book.html', {'form': form})

def cancel_appointment(request):
    if request.method == 'POST':
        form = CancelForm(request.POST)
        if form.is_valid():
            key = form.cleaned_data['key']
            try:
                guest = Guest.objects.get(key=key)
                slot = guest.appointment
                slot.is_open = True
                slot.guest_key = ""
                slot.save()
                guest.delete()
                return render(request, 'appointments/cancelled.html', {'key': key})
            except Guest.DoesNotExist:
                form.add_error('key', 'Invalid key')
    else:
        form = CancelForm()
    return render(request, 'appointments/cancel.html', {'form': form})
