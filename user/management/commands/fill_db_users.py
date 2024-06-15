from django.core.management.base import BaseCommand
from user.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):

        # User.objects.all().delete()

        print("Filling db ...")

        User.objects.create_user(
            username="artyombn",
            first_name="Andrei",
            last_name="Pushkin",
            age=21,
            email="pushka@gmail.com",
            password='admin',
            is_staff=True,
        ),
        User.objects.create_superuser(
            username="admin",
            first_name="Kolia",
            last_name="Tokaev",
            age=27,
            email="tokaaa@gmail.com",
            password='admin',
            is_staff=True,
        ),


        print("Done")

        print(User.objects.all())

