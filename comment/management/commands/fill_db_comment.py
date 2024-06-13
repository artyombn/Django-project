from django.core.management.base import BaseCommand
from comment.models import Comment
from idea.models import Idea
from user.models import User

class Command(BaseCommand):
    def handle(self, *args, **options):

        Comment.objects.all().delete()

        print("Filling db with comments...")

        # нужно будет потом настроить сессию, чтобы получать user из формы комментария
        user = User.objects.get(username='artyombn')

        comments_data = [
            {
                "author": user,
                "text": "Random comment 1",
            },
            {
                "author": user,
                "text": "Random comment 2",
            },
        ]

        comments = []
        for comment_data in comments_data:
            comment = Comment(**comment_data)
            comments.append(comment)

        Comment.objects.bulk_create(comments)

        ideas = Idea.objects.filter(author=user)

        for comment in comments:
            comment.idea.add(*ideas)

        print("Done")

        print(Idea.objects.all())
