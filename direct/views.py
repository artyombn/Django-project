from django.views.generic import ListView
from django.views.generic.base import View
from django.db.models import Q

from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import JsonResponse

from .models import Message, User

class MessagesList(ListView):
    model = Message
    template_name = 'messages/list.html'

    def all_user_messages(self):
        user = self.request.user
        return Message.objects.filter(Q(sender=user) | Q(recipient=user)).order_by('date')


    # def user_messages(self):
    #     user = self.request.user
    #     recipient = Message.objects.filter(recipient=user)
    #     sender = Message.objects.filter(sender=user)
    #     all_user_messages = []
    #     for m in recipient:
    #         all_user_messages.append(m)
    #     for n in sender:
    #         all_user_messages.append(n)
    #     return all_user_messages

    def all_users(self):
        user = self.request.user
        messages = self.all_user_messages()
        users = []
        users_set = set()
        for us in messages:
            if us.sender != user and us.sender not in users_set:
                users.append(us.sender)
                users_set.add(us.sender)
            if us.recipient != user and us.recipient not in users_set:
                users.append(us.recipient)
                users_set.add(us.recipient)
        return users

    def messages_by_user(self):
        user = self.request.user
        users = self.all_users()
        messages = self.all_user_messages()
        messages_by_user = {}
        for message in messages:
            if message.sender != user:
                if message.sender not in messages_by_user:
                    messages_by_user[message.sender] = []
                messages_by_user[message.sender].append(message)

            if message.recipient != user:
                if message.recipient not in messages_by_user:
                    messages_by_user[message.recipient] = []
                messages_by_user[message.recipient].append(message)

        return messages_by_user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_user_messages = self.all_user_messages()
        all_users = self.all_users()
        messages_by_user = self.messages_by_user()
        context['user'] = self.request.user
        context['all_messages'] = Message.objects.all()
        context['all_user_messages'] = all_user_messages
        context['all_users'] = all_users
        context['messages_by_user'] = messages_by_user
        return context


class LoadMessagesView(MessagesList):
    def get(self, request, *args, **kwargs):
        user_id = self.request.GET.get('user_id')
        if not user_id:
            return JsonResponse({'error': 'user_id not provided'}, status=400)

        user = self.request.user

        messages = Message.objects.filter((Q(sender_id=user_id) & Q(recipient=user)) | (Q(recipient_id=user_id) & Q(sender=user))).order_by('date')

        messages_data = []
        for message in messages:
            messages_data.append({
                'sender_id': message.sender_id,
                'recipient_id': message.recipient_id,
                'content': message.content,
                'date': message.date.isoformat(),
                'sender_name': message.sender.username,
            })

        return JsonResponse({'messages': messages_data})