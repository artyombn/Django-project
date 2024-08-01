from django.core.management.base import BaseCommand

from direct.models import Message
from user.models import User

class Command(BaseCommand):
    def handle(self, *args, **options):

        Message.objects.all().delete()

        print("Filling db Messages...")

        artyombn = User.objects.get(username='artyombn')
        user = User.objects.get(username='user')
        test = User.objects.get(username='test')


        messages_data = [
            {
                "sender": user,
                "recipient": artyombn,
                "content": "Hi Artem! How are you?",
            },
            {
                "sender": artyombn,
                "recipient": user,
                "content": "Hey Anna) I'm doing well. What about you?",
            },
            {
                "sender": user,
                "recipient": artyombn,
                "content": "Everything is ok for me too, thanks. Any plans for today?",
            },
            {
                "sender": artyombn,
                "recipient": user,
                "content": "Not yet. Let's meet  today!",
            },
            {
                "sender": test,
                "recipient": artyombn,
                "content": "Hey bro! I need your help)",
            },
            {
                "sender": artyombn,
                "recipient": test,
                "content": "Hi bro) what kind of help are you talking about?",
            },
            {
                "sender": test,
                "recipient": artyombn,
                "content": "I will share the details a bit later) see you",
            },
            {
                "sender": artyombn,
                "recipient": test,
                "content": "Deal!",
            },
            {
                "sender": user,
                "recipient": test,
                "content": "Hey Hey!!!",
            },
            {
                "sender": test,
                "recipient": user,
                "content": "I'm here) What would you like?",
            },
        ]

        messages = []
        for message in messages_data:
            m = Message(**message)
            messages.append(m)

        Message.objects.bulk_create(messages)

        print("Done")
