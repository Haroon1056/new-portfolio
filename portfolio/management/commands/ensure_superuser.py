from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from decouple import config

class Command(BaseCommand):
    help = 'Ensure a superuser exists'

    def handle(self, *args, **options):
        username = config('DJANGO_SUPERUSER_USERNAME', default='Nimra')
        email = config('DJANGO_SUPERUSER_EMAIL', default='nimranaseeb101@gmail.com')
        password = config('DJANGO_SUPERUSER_PASSWORD', default='nimra')
        
        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username, email, password)
            self.stdout.write(self.style.SUCCESS(f'Superuser "{username}" created successfully!'))
        else:
            self.stdout.write(self.style.SUCCESS(f'Superuser "{username}" already exists.'))