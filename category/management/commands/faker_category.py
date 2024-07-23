from django.core.management.base import BaseCommand
from faker import Faker


class Command(BaseCommand):
    help = "Learn Faker"

    def handle(self, *args, **kwargs):
        from category.models import Category
        from user.models import User

        fake = Faker('ru_Ru')

        class FakerFactory():
            def fake_category(self):
                title = fake.company()
                description = fake.text()

                print(f"Category: {title=}, {description=}")


            def fake_user(self):
                username = fake.user_name()
                first_name = fake.first_name()
                last_name = fake.last_name()
                age = fake.random_int(min=18, max=99)
                email = fake.email()

                print(f"User: {username=}, {first_name=}, {last_name=}, {age=}, {email=}")

        factory = FakerFactory()
        factory.fake_category()
        factory.fake_user()