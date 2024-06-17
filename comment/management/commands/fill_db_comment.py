from django.core.management.base import BaseCommand
from comment.models import Comment
from idea.models import Idea
from user.models import User

class Command(BaseCommand):
    def handle(self, *args, **options):

        Comment.objects.all().delete()

        print("Filling db Comments...")

        # нужно будет потом настроить сессию, чтобы получать user из формы комментария
        user1 = User.objects.get(username='artyombn')
        user2 = User.objects.get(username='user')

        ideas1 = Idea.objects.filter(author=user1)
        ideas2 = Idea.objects.filter(author=user2)

        if not ideas1.exists():
            print("This user doesn't have any Ideas")
            return

        if not ideas2.exists():
            print("This user doesn't have any Ideas")
            return

        idea1 = ideas1[0]
        idea2 = ideas1[0]

        comments_data1 = [
            {
                "author": user1,
                "text": "Random comment #1",
                "idea": idea1,
            },
            {
                "author": user1,
                "text": "Random comment #2",
                "idea": idea1,
            },
        ]

        comments_data2 = [
            {
                "author": user2,
                "text": "Random comment #1",
                "idea": idea2,
            },
            {
                "author": user2,
                "text": "Random comment #2",
                "idea": idea2,
            },
        ]

        comments1 = []
        for comment_data in comments_data1:
            comment = Comment(**comment_data)
            comments1.append(comment)

        Comment.objects.bulk_create(comments1)

        comments2 = []
        for comment_data in comments_data2:
            comment = Comment(**comment_data)
            comments2.append(comment)

        Comment.objects.bulk_create(comments2)

        print("Done")
