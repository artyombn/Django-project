from django.core.management.base import BaseCommand
from user.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):

        User.objects.all().delete()

        print("Filling db Users...")

        User.objects.create_superuser(
            username="artyombn",
            first_name="Artyom",
            last_name="Balabashin",
            age=21,
            email="balabashin@gmail.com",
            password='admin',
            is_staff=True,
        ),
        User.objects.create_user(
            username="user",
            first_name="Kolia",
            last_name="Tokaev",
            age=27,
            email="tokaaa@gmail.com",
            password='user',
        ),


        print("Done")

        print(User.objects.all())

