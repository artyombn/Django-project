from django.core.management.base import BaseCommand
from partnership.models import CoAuthor, PreCoAuthor
from idea.models import Idea
from user.models import User

class Command(BaseCommand):
    def handle(self, *args, **options):

        CoAuthor.objects.all().delete()

        print("Filling db Partnerships...")

        artyombn = User.objects.get(username="artyombn")
        user = User.objects.get(username="user")


        idea1 = Idea.objects.get(title="FinTechHub")
        idea2 = Idea.objects.get(title="CodeForKids")
        idea3 = Idea.objects.get(title="HealthCareAI")
        idea4 = Idea.objects.get(title="BlockchainStartup")

        coauthors = [
            CoAuthor(idea=idea1,
                 user=user,
                 role="QA",
                 ),
            CoAuthor(idea=idea3,
                 user=artyombn,
                 role="Publisher",
                 ),
            CoAuthor(idea=idea4,
                 user=user,
                 role="OM",
                 ),
        ]

        CoAuthor.objects.bulk_create(coauthors)

        PreCoAuthor.objects.create(
            idea=idea2,
            user=artyombn,
        )

        idea5 = Idea.objects.get(title="OnlineEducationPlatform")
        PreCoAuthor.objects.create(
            idea=idea5,
            user=user,
        )

        print("Done")