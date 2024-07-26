from django.core.management.base import BaseCommand
from user.models import User
from idea.models import Idea
from notifications.models import Notification

class Command(BaseCommand):
    def handle(self, *args, **options):

        Notification.objects.all().delete()

        print("Filling db Notifications...")

        artyombn = User.objects.get(username="artyombn")
        user = User.objects.get(username="user")
        test = User.objects.get(username="test")

        idea1 = Idea.objects.get(title="CodeForKids")
        idea2 = Idea.objects.get(title="OnlineEducationPlatform")
        idea3 = Idea.objects.get(title="FinTechHub")
        idea4 = Idea.objects.get(title="DesignExchange")
        idea5 = Idea.objects.get(title="HealthCareAI")
        idea6 = Idea.objects.get(title="MentalWellnessCommunity")

        notifications = [
            Notification(
                sender=user,
                user=artyombn,
                notification_type=4,
            ),
            Notification(
                sender=test,
                user=artyombn,
                notification_type=4,
            ),
            Notification(
                sender=artyombn,
                user=user,
                notification_type=4,
            ),
            Notification(
                idea=idea1,
                sender=artyombn,
                user=user,
                notification_type=5,
            ),
            Notification(
                idea=idea2,
                sender=user,
                user=artyombn,
                notification_type=5,
            ),
            Notification(
                idea=idea2,
                sender=user,
                user=user,
                notification_type=5,
            ),
            Notification(
                idea=idea1,
                sender=artyombn,
                user=artyombn,
                notification_type=5,
            ),
            Notification(
                idea=idea3,
                sender=user,
                user=artyombn,
                notification_type=1,
            ),
            Notification(
                idea=idea3,
                sender=test,
                user=artyombn,
                notification_type=2,
            ),
            Notification(
                idea=idea1,
                sender=test,
                user=user,
                notification_type=1,
            ),
            Notification(
                idea=idea1,
                sender=artyombn,
                user=user,
                notification_type=1,
            ),
            Notification(
                idea=idea4,
                sender=user,
                user=test,
                notification_type=1,
            ),
            Notification(
                idea=idea4,
                sender=artyombn,
                user=test,
                notification_type=2,
            ),
            Notification(
                idea=idea2,
                sender=artyombn,
                user=user,
                notification_type=9,
            ),
            Notification(
                idea=idea2,
                sender=artyombn,
                user=test,
                notification_type=9,
            ),
            Notification(
                idea=idea5,
                sender=user,
                user=artyombn,
                notification_type=9,
            ),
            Notification(
                idea=idea3,
                sender=user,
                user=artyombn,
                text_preview="Hi Artem! Thanks for this Idea. I liked it and added to my favourite",
                notification_type=3,
            ),
            Notification(
                idea=idea3,
                sender=test,
                user=artyombn,
                text_preview="There are many other interesting Ideas. I disliked it. Sorry bro",
                notification_type=3,
            ),
            Notification(
                idea=idea1,
                sender=artyombn,
                user=test,
                text_preview="Yeep. totally agree",
                notification_type=3,
            ),
            Notification(
                idea=idea1,
                sender=test,
                user=test,
                text_preview="I'm interested in this because my son loves coding!",
                notification_type=3,
            ),
            Notification(
                idea=idea5,
                sender=artyombn,
                user=artyombn,
                notification_type=6,
            ),
            Notification(
                idea=idea4,
                sender=artyombn,
                user=artyombn,
                notification_type=7,
            ),
            Notification(
                idea=idea6,
                sender=user,
                user=artyombn,
                notification_type=8,
            ),
        ]

        Notification.objects.bulk_create(notifications)

        print("Done")