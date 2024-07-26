from django.views.generic import ListView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Min
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.db.models.signals import post_save, post_delete
from django.views import View

from idea.models import Idea
from .forms import PreCoAuthorForm
from partnership.models import CoAuthor, PreCoAuthor
from notifications.models import Notification


class CoAuthorsView(LoginRequiredMixin, ListView):
    model = CoAuthor
    template_name = 'partnership/coauthors.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        idea_coauthors_dict = {}

        ideas = Idea.objects.annotate(
            earliest_joined_at=Min('coauthor__joined_at')
        ).order_by('-earliest_joined_at')
        ideas_dict = {idea: list(idea.co_author.all()) for idea in ideas}
        new_list = []
        for idea_id, coauthor in ideas_dict.items():
            if coauthor:
                new_list.append([idea_id, coauthor])
                # print(f'new list = {new_list}')
                # print(f'coauthor = {coauthor}')

        idea_enumerate = enumerate(new_list, start=1)

        users = []
        us_list = []
        ideas_list = [] # [<Idea: CodeForKids/Society/user>, <Idea: Creative4343/Creative/artyombn>]
        final_users = set()
        model_ideas = {}
        for query in new_list: # [[<Idea: CodeForKids/Society/user>, [<User: test>, <User: artyombn>]], [<Idea: Creative4343/Creative/artyombn>, [<User: user>, <User: test>]]]
            ideas_list.append(query[0])
            for elements in query[1]:
                user = CoAuthor.objects.filter(user=elements, idea=query[0])
                users.append(user)
            us_list.append(list(users))
            users.clear()


        coauthor_list = [] # [<CoAuthor: test - CodeForKids - >, <CoAuthor: artyombn - CodeForKids - >, <CoAuthor: user - Creative4343 - Developer>, <CoAuthor: test - Creative4343 - >]
        for us22 in us_list:
            for q in us22:
                for t in q:
                    # print(f'us = {t} type - {type(t)}')
                    # print(f'idea title = {t.idea}')
                    coauthor_list.append(t)

            for coauthor in coauthor_list:
                idea = coauthor.idea
                if idea in ideas:
                    if idea not in idea_coauthors_dict:
                        idea_coauthors_dict[idea] = []
                        idea_coauthors_dict[idea].append(coauthor)
                    else:
                        idea_coauthors_dict[idea].append(coauthor)


        context['idea_enumerate'] = idea_enumerate
        context['model_coauthor'] = model_ideas
        context['idea_coauthors_dict'] = idea_coauthors_dict
        context['coauthor_list'] = coauthor_list

        return context



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

        next_page = request.GET.get('next', 'ideas:detail')
        if next_page == 'ideas:detail':
            return redirect('ideas:detail', pk=idea.pk)
        elif next_page == 'users:partnerships':
            return redirect('users:partnerships', pk=user.id)
        else:
            return redirect('ideas:detail', pk=idea.pk)

class CoAuthorDeleteView(View):
    def post(self, request, pk):
        idea = get_object_or_404(Idea, pk=pk)
        user = request.user

        coauthor = CoAuthor.objects.filter(idea=idea, user=user)
        coauthor.delete()

        return redirect('ideas:detail', pk=idea.pk)