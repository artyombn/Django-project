from django.core.management.base import BaseCommand
from user.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):

        User.objects.all().delete()

        print("Filling db ...")

        users_list = [
            User(username="artyombn",
                 first_name="Artem",
                 last_name="Balabashin",
                 email="balabashinan@gmail.com")
        ]

        User.objects.bulk_create(users_list)

        print("Done")

        print(User.objects.all())

