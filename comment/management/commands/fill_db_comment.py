from django.core.management.base import BaseCommand
from comment.models import Comment, CommentLikes
from idea.models import Idea
from user.models import User

class Command(BaseCommand):
    def handle(self, *args, **options):

        Comment.objects.all().delete()

        print("Filling db Comments...")

        artyombn = User.objects.get(username='artyombn')
        user = User.objects.get(username='user')
        test = User.objects.get(username='test')

        idea1 = Idea.objects.get(title="FinTechHub")
        idea2 = Idea.objects.get(title="CodeForKids")
        idea3 = Idea.objects.get(title="DesignExchange")


        comments_data1 = [
            {
                "author": artyombn,
                "text": "Hi everyone! Welcome to my first Idea. Feel free to discuss anything",
                "idea": idea1,
            },
            {
                "author": user,
                "text": "Hi Artem! Thanks for this Idea. I liked it and added to my favourite",
                "idea": idea1,
            },
            {
                "author": test,
                "text": "There are many other interesting Ideas. I disliked it. Sorry bro",
                "idea": idea1,
            },
            {
                "author": artyombn,
                "text": "No problem, bro! I'm ok with any negative comments",
                "idea": idea1,
            },
            {
                "author": test,
                "text": "Glad to hear it! Good luck with your Idea!",
                "idea": idea1,
            },
            {
                "author": artyombn,
                "text": "Thanks!)",
                "idea": idea1,
            },
        ]

        comments_data2 = [
            {
                "author": user,
                "text": "This is a really good opportunity for Kids to get knowledge how do coding, isn't it?",
                "idea": idea2,
            },
            {
                "author": artyombn,
                "text": "Yeep. totally agree",
                "idea": idea2,
            },
            {
                "author": test,
                "text": "I'm interested in this because my son loves coding!",
                "idea": idea2,
            },
            {
                "author": user,
                "text": "Great! Let's develop this idea together",
                "idea": idea2,
            },
        ]

        comments_data3 = [
            {
                "author": test,
                "text": "This Idea can help designers to improve their skills",
                "idea": idea3,
            },
            {
                "author": artyombn,
                "text": "I'm bad at design, so I will just miss this Idea",
                "idea": idea3,
            },
            {
                "author": user,
                "text": "I don't mind to try to implement this idea. Let's try!",
                "idea": idea3,
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

        comments3 = []
        for comment_data in comments_data3:
            comment = Comment(**comment_data)
            comments3.append(comment)

        Comment.objects.bulk_create(comments3)


        # Idea 1
        comment1 = Comment.objects.get(id=1)
        comment2 = Comment.objects.get(id=2)
        comment3 = Comment.objects.get(id=4)
        comment4 = Comment.objects.get(id=5)

        comment_likes1 = [
            CommentLikes(
                author=user,
                comment=comment1,
                 ),
            CommentLikes(
                author=artyombn,
                comment=comment2,
            ),
            CommentLikes(
                author=test,
                comment=comment3,
            ),
            CommentLikes(
                author=artyombn,
                comment=comment4,
            ),
            CommentLikes(
                author=user,
                comment=comment4,
            ),
        ]

        CommentLikes.objects.bulk_create(comment_likes1)

        # Idea 2
        comment7 = Comment.objects.get(id=7)
        comment8 = Comment.objects.get(id=8)
        comment9 = Comment.objects.get(id=9)
        comment10 = Comment.objects.get(id=10)

        comment_likes2 = [
            CommentLikes(
                author=artyombn,
                comment=comment7,
            ),
            CommentLikes(
                author=test,
                comment=comment7,
            ),
            CommentLikes(
                author=user,
                comment=comment8,
            ),
            CommentLikes(
                author=user,
                comment=comment9,
            ),
            CommentLikes(
                author=test,
                comment=comment10,
            ),
            CommentLikes(
                author=artyombn,
                comment=comment10,
            ),
        ]

        CommentLikes.objects.bulk_create(comment_likes2)


        # Idea 3
        comment11 = Comment.objects.get(id=11)
        comment13 = Comment.objects.get(id=13)

        comment_likes3 = [
            CommentLikes(
                author=user,
                comment=comment11,
            ),
            CommentLikes(
                author=test,
                comment=comment13,
            ),
        ]

        CommentLikes.objects.bulk_create(comment_likes3)


        print("Done")
