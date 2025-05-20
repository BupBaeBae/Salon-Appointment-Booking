
from django.core.management.base import BaseCommand
from appointments.models import Artist, Slot
from datetime import time

class Command(BaseCommand):
    help = 'Preload artist and slot data with manicure and pedicure options'

    def handle(self, *args, **kwargs):
        artists = ["Ngoc", "Hong"]
        time_slots = [
            ("09:00", "9:00 a.m"),
            ("09:20", "9:20 a.m"),
            ("09:40", "9:40 a.m"),
            ("10:00", "10:00 a.m"),
            ("10:20", "10:20 a.m"),
        ]

        services = ["manicure", "pedicure"]

        for artist_name in artists:
            artist, _ = Artist.objects.get_or_create(name=artist_name)
            for service in services:
                for t_str, label in time_slots:
                    h, m = map(int, t_str.split(":"))
                    Slot.objects.get_or_create(
                        artist=artist,
                        service_type=service,
                        time=time(h, m),
                        defaults={
                            'slot_label': label,
                            'is_open': True,
                        }
                    )

        self.stdout.write(self.style.SUCCESS("Successfully preloaded manicure and pedicure slots without duplication."))
