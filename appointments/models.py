
from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Slot(models.Model):
    SERVICE_TYPES = [
        ('manicure', 'Manicure'),
        ('pedicure', 'Pedicure'),
    ]

    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    service_type = models.CharField(max_length=20, choices=SERVICE_TYPES)
    time = models.TimeField()
    slot_label = models.CharField(max_length=20)
    is_open = models.BooleanField(default=True)
    guest_key = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.artist.name} - {self.slot_label} ({'Open' if self.is_open else 'Booked'})"

class Guest(models.Model):
    name = models.CharField(max_length=100)
    appointment = models.ForeignKey(Slot, on_delete=models.CASCADE)
    key = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.name} - {self.key}"
