from django.core.management.base import BaseCommand
from idea.models import Idea, IdeaStatus
from category.models import Category
from user.models import User

class Command(BaseCommand):
    def handle(self, *args, **options):

        Idea.objects.all().delete()

        print("Filling db IdeaStatuses...")

        artyombn = User.objects.get(username="artyombn")

        statuses = [
            IdeaStatus(status="active",
            updated_by=artyombn,
            ),
            IdeaStatus(status="pending",
            updated_by=artyombn,
            ),
            IdeaStatus(status="completed",
            updated_by=artyombn,
            ),
            ]

        IdeaStatus.objects.bulk_create(statuses)

        active_status = IdeaStatus.objects.get(status="active")
        pending_status = IdeaStatus.objects.get(status="pending")
        completed_status = IdeaStatus.objects.get(status="completed")

        ideas = [
            Idea(title="FinTechHub",
                 description="Track your finance with advanced AI algorithms and blockchain technology.",
                 category=Category.objects.get(title="Technology"),
                 author=User.objects.get(username="artyombn"),
                 image='/idea_images/example1.jpeg',
                 status=active_status,
                 ),
            Idea(title="CodeForKids",
                 description="Teach programming to children through interactive games and educational materials.",
                 category=Category.objects.get(title="Society"),
                 author=User.objects.get(username="user"),
                 image='/idea_images/example2.jpg',
                 status=active_status,
                 ),
            Idea(title="DesignExchange",
                 description="Create a platform for designers to exchange ideas, collaborate on projects, and showcase their work.",
                 category=Category.objects.get(title="Creative"),
                 author=User.objects.get(username="test"),
                 image='/idea_images/example3.png',
                 status=pending_status,
                 ),
            Idea(title="HealthCareAI",
                 description="Develop an AI-powered healthcare system to diagnose diseases early and improve patient outcomes.",
                 category=Category.objects.get(title="Health"),
                 author=User.objects.get(username="user"),
                 status=completed_status,
                 ),
            Idea(title="BlockchainStartup",
                 description="Start a blockchain-based startup to revolutionize digital transactions and secure data.",
                 category=Category.objects.get(title="Finance"),
                 author=User.objects.get(username="test"),
                 status=pending_status,
                 ),
            Idea(title="OnlineEducationPlatform",
                 description="Build an online platform offering courses on various subjects to empower lifelong learning.",
                 category=Category.objects.get(title="Education"),
                 author=User.objects.get(username="artyombn"),
                 status=completed_status,
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