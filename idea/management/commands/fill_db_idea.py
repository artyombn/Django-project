from django.core.management.base import BaseCommand
from idea.models import Idea
from category.models import Category
from user.models import User

class Command(BaseCommand):
    def handle(self, *args, **options):

        Idea.objects.all().delete()

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
                 author=User.objects.get(username="user"),
                 ),
            Idea(title="DesignExchange",
                 description="Create and share your design",
                 category=Category.objects.get(title="Creative"),
                 author=User.objects.get(username="artyombn"),
                 ),
            Idea(title="TestIdea#2",
                 description="TestIdea#2 description here. You can choose this idea or share another one to find partnership of investments.",
                 category=Category.objects.get(title="Creative"),
                 author=User.objects.get(username="user"),
                 ),
            Idea(title="TestIdea#3",
                 description="TestIdea#3 description here. You can choose this idea or share another one to find partnership of investments.",
                 category=Category.objects.get(title="Creative"),
                 author=User.objects.get(username="user"),
                 ),
            Idea(title="TestIdea#4",
                 description="TestIdea#4 description here. You can choose this idea or share another one to find partnership of investments.",
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