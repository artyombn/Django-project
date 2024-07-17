from django.views.generic import ListView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.db.models.signals import post_save, post_delete
from django.views import View

from idea.models import Idea
from .forms import PreCoAuthorForm
from partnership.models import CoAuthor, PreCoAuthor
from notifications.models import Notification


class CoAuthorsView(ListView):
    model = CoAuthor
    template_name = 'partnership/coauthors.html'


class PreCoAuthorView(CreateView):
    model = PreCoAuthor
    form_class = PreCoAuthorForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.idea = get_object_or_404(Idea, pk=self.kwargs.get("pk"))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('ideas:detail', kwargs={'pk': self.object.idea.pk})


class PreCoAuthorDeleteView(DeleteView):
    model = PreCoAuthor

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('ideas:detail', kwargs={'pk': self.object.idea.pk})

class ApproveCoAuthor(View):
    def post(self, request, notification_id):
        notification = get_object_or_404(Notification, id=notification_id)
        idea = notification.idea
        user = notification.sender

        CoAuthor.objects.create(idea=idea, user=user)
        precoauthor = PreCoAuthor.objects.filter(idea=idea, user=user)
        precoauthor.delete()

        return redirect('notifications:show-notifications')


class RejectCoAuthor(View):
    def post(self, request, notification_id):
        notification = get_object_or_404(Notification, id=notification_id)
        idea = notification.idea
        user = notification.sender

        precoauthor = PreCoAuthor.objects.filter(idea=idea, user=user).first()
        if precoauthor:
            precoauthor.is_rejected = True
            precoauthor.save()
            precoauthor.delete()

        return redirect('notifications:show-notifications')



class StopBeingCoAuthor(View):
    def post(self, request, pk):
        idea = get_object_or_404(Idea, pk=pk)
        user = request.user

        coauthor = CoAuthor.objects.filter(idea=idea, user=user)
        coauthor.delete()

        return redirect('ideas:detail', pk=idea.pk)


