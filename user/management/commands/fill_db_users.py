from django.core.management.base import BaseCommand
from user.models import User, Follow
from django.contrib.auth.models import Group


class Command(BaseCommand):
    def handle(self, *args, **options):

        User.objects.all().delete()
        Group.objects.all().delete()
        Follow.objects.all().delete()


        print("Filling db Users...")

        artyombn = User.objects.create_superuser(
            username="artyombn",
            first_name="Artyom",
            last_name="Balabashin",
            age=29,
            email="balabashinan@gmail.com",
            password='admin',
            avatar='/user_avatars/man-avatar.png',
        )

        user2 = User.objects.create_user(
            username="user",
            first_name="Anna",
            last_name="Dmitrieva",
            age=27,
            email="annadm@gmail.com",
            password='user',
            avatar='/user_avatars/woman-avatar.png',
        )
        user3 = User.objects.create_user(
            username="test",
            first_name="Anton",
            last_name="Makarov",
            age=31,
            email="anmakarov@gmail.com",
            password='test',
        )

        print("Users created")
        print(User.objects.all())


        follows = [
            Follow(follower=artyombn,
                   following=user2,
                   ),
            Follow(follower=user2,
                   following=artyombn,
                   ),
            Follow(follower=artyombn,
                   following=user3,
                   ),
        ]

        Follow.objects.bulk_create(follows)


        admin_group, created = Group.objects.get_or_create(name="Admin")
        moderator_group, created = Group.objects.get_or_create(name="Moderator")
        user_group, created = Group.objects.get_or_create(name="User")
        co_author_group, created = Group.objects.get_or_create(name="Co-Author")
        investor_group, created = Group.objects.get_or_create(name="Investor")
        verified_group, created = Group.objects.get_or_create(name="Verified")

        print("Groups created")

        artyombn.groups.add(user_group, admin_group, verified_group)
        user2.groups.add(user_group, investor_group, verified_group)



