from django.core.management.base import BaseCommand
from idea.models import Idea
from category.models import Category
from user.models import User

class Command(BaseCommand):
    def handle(self, *args, **options):

        # Idea.objects.all().delete()

        print("Filling db Ideas...")

        ideas = [
            Idea(title="FinTechHub",
                 description="Track your finance",
                 category=Category.objects.get(title="Tech"),
                 author=User.objects.get(username="artyombn"),
                 ),
            Idea(title="CodeForKids",
                 description="Teach your kids to be programmer",
                 category=Category.objects.get(title="Society"),
                 author=User.objects.get(username="artyombn"),
                 ),
            Idea(title="DesignExchange",
                 description="Create and share your design",
                 category=Category.objects.get(title="Creative"),
                 author=User.objects.get(username="artyombn"),
                 ),
        ]

        Idea.objects.bulk_create(ideas)

        print("Done")

        print(Idea.objects.all())

        # print("Updating idea FinTechHub")
        # FinTechHub_update = Idea.objects.get(title="FinTechHub")
        # FinTechHub_update.description = "Manage your personal finances"
        # FinTechHub_update.save()
        # print("Updated")

        print(Idea.objects.all())