from django.core.management.base import BaseCommand
from idea.models import Idea, IdeaStatus, Likes, DisLikes, Favourite
from category.models import Category
from user.models import User

class Command(BaseCommand):
    def handle(self, *args, **options):

        Idea.objects.all().delete()

        print("Filling db IdeaStatuses...")

        artyombn = User.objects.get(username="artyombn")
        user = User.objects.get(username="user")
        test = User.objects.get(username="test")

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
                 author=artyombn,
                 image='/idea_images/example1.jpeg',
                 status=active_status,
                 ),
            Idea(title="CodeForKids",
                 description="Teach programming to children through interactive games and educational materials.",
                 category=Category.objects.get(title="Society"),
                 author=user,
                 image='/idea_images/example2.png',
                 status=active_status,
                 ),
            Idea(title="DesignExchange",
                 description="Create a platform for designers to exchange ideas, collaborate on projects, and showcase their work.",
                 category=Category.objects.get(title="Creative"),
                 author=test,
                 image='/idea_images/example3.png',
                 status=pending_status,
                 ),
            Idea(title="HealthCareAI",
                 description="Develop an AI-powered healthcare system to diagnose diseases early and improve patient outcomes.",
                 category=Category.objects.get(title="Health"),
                 author=user,
                 image='/idea_images/example4.jpeg',
                 status=completed_status,
                 ),
            Idea(title="BlockchainStartup",
                 description="Start a blockchain-based startup to revolutionize digital transactions and secure data.",
                 category=Category.objects.get(title="Finance"),
                 author=test,
                 image='/idea_images/example5.jpeg',
                 status=pending_status,
                 ),
            Idea(title="OnlineEducationPlatform",
                 description="Build an online platform offering courses on various subjects to empower lifelong learning.",
                 category=Category.objects.get(title="Education"),
                 author=artyombn,
                 image='/idea_images/example6.jpg',
                 status=completed_status,
                 ),
            Idea(title="SmartHomeAutomation",
                 description="Design a smart home automation system that integrates various IoT devices to enhance home security and convenience.",
                 category=Category.objects.get(title="Technology"),
                 author=user,
                 status=pending_status,
                 ),

            Idea(title="MentalWellnessCommunity",
                 description="Establish an online community that provides resources, support, and activities for mental wellness and mindfulness.",
                 category=Category.objects.get(title="Society"),
                 author=artyombn,
                 status=active_status,
                 ),

        ]

        Idea.objects.bulk_create(ideas)

        # Likes

        idea1 = Idea.objects.get(id=1)
        idea2 = Idea.objects.get(id=2)
        idea3 = Idea.objects.get(id=3)
        idea4 = Idea.objects.get(id=4)

        likes = [
            Likes(
                idea=idea1,
                author=artyombn,
                 ),
            Likes(
                idea=idea1,
                author=user,
            ),
            Likes(
                idea=idea2,
                author=artyombn,
            ),
            Likes(
                idea=idea2,
                author=test,
            ),
            Likes(
                idea=idea3,
                author=user,
            ),
            ]

        Likes.objects.bulk_create(likes)

        # DisLikes

        dislikes = [
            DisLikes(
                idea=idea1,
                author=test,
            ),
            DisLikes(
                idea=idea3,
                author=artyombn,
            ),
        ]

        DisLikes.objects.bulk_create(dislikes)

        # Favourites

        favourites = [
            Favourite(
                idea=idea1,
                user=user,
                 ),
            Favourite(
                idea=idea1,
                user=test,
            ),
            Favourite(
                idea=idea2,
                user=artyombn,
            ),
            Favourite(
                idea=idea4,
                user=artyombn,
            ),
            Favourite(
                idea=idea2,
                user=test,
            ),
        ]

        Favourite.objects.bulk_create(favourites)