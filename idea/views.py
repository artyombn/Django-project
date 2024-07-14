from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.db.models import Count
from django.views.generic.base import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django_filters.views import FilterView
from .filters import IdeaFilter

from category.models import Category
from comment.forms import CommentForm
from .models import Idea, Likes, DisLikes, IdeaStatus
from .forms import IdeasForm
from user.group_permission import GroupRequiredMixin


def index(request):
    ideas = Idea.objects.all()
    categories = Category.objects.all()
    statuses = IdeaStatus.objects.all()

    category = request.GET.get('category')
    status = request.GET.get('status')
    sort = request.GET.get('sort')
    sort_choice = [
        ('1', 'MostLiked'),
        ('2', 'MostCommented'),
        ('3', 'DateAscending'),
        ('4', 'DateDescending'),
    ]
    co_authors = request.GET.get('co_authors')
    investors = request.GET.get('investors')

    def check_co_authors_and_investors(ideas, co_authors, investors):
        if co_authors and investors:
            ideas = ideas.filter(coauthor__isnull=False, investors__isnull=False).distinct()
        elif co_authors:
            ideas = ideas.filter(coauthor__isnull=False).distinct()
        elif investors:
            ideas = ideas.filter(investors__isnull=False).distinct()
        else:
            ideas = ideas

        return ideas

    if sort:
        last_idea = check_co_authors_and_investors(ideas, co_authors, investors)

        if sort == sort_choice[0][0]:
            if category and status:
                ideas = last_idea.filter(category=category, status__status=status).annotate(num_likes=Count('likes__id')).order_by('-num_likes')
            elif category:
                ideas = last_idea.filter(category=category).annotate(num_likes=Count('likes__id')).order_by('-num_likes')
            elif status:
                ideas = last_idea.filter(status__status=status).annotate(num_likes=Count('likes__id')).order_by('-num_likes')
            else:
                ideas = last_idea.annotate(num_likes=Count('likes__id')).order_by('-num_likes')


        elif sort == sort_choice[1][0]:
            last_idea = check_co_authors_and_investors(ideas, co_authors, investors)

            if category and status:
                ideas = last_idea.filter(category=category, status__status=status).annotate(num_comments=Count('comments')).order_by('-num_comments')
            elif category:
                ideas = last_idea.filter(category=category).annotate(num_comments=Count('comments')).order_by('-num_comments')
            elif status:
                ideas = last_idea.filter(status__status=status).annotate(num_comments=Count('comments')).order_by('-num_comments')
            else:
                ideas = last_idea.annotate(num_comments=Count('comments')).order_by('-num_comments')


        elif sort == sort_choice[2][0]:
            last_idea = check_co_authors_and_investors(ideas, co_authors, investors)

            if category and status:
                ideas = last_idea.filter(category=category, status__status=status).order_by('created_at')
            elif category:
                ideas = last_idea.filter(category=category).order_by('created_at')
            elif status:
                ideas = last_idea.filter(status__status=status).order_by('created_at')
            else:
                ideas = last_idea.order_by('created_at')

        else:
            last_idea = check_co_authors_and_investors(ideas, co_authors, investors)

            if category and status:
                ideas = last_idea.filter(category=category, status__status=status).order_by('-created_at')
            elif category:
                ideas = last_idea.filter(category=category).order_by('-created_at')
            elif status:
                ideas = last_idea.filter(status__status=status).order_by('-created_at')
            else:
                ideas = last_idea.order_by('-created_at')


    elif category and status:
        last_idea = check_co_authors_and_investors(ideas, co_authors, investors)

        ideas = last_idea.filter(category=category, status__status=status)
    elif category:
        last_idea = check_co_authors_and_investors(ideas, co_authors, investors)

        ideas = last_idea.filter(category=category)
    elif status:
        last_idea = check_co_authors_and_investors(ideas, co_authors, investors)

        ideas = last_idea.filter(status__status=status)
    else:
        last_idea = check_co_authors_and_investors(ideas, co_authors, investors)

        ideas = last_idea


    context = {
        'ideas': ideas,
        'categories': categories,
        'statuses': statuses,
        'sort': sort_choice
    }
    return render(request, 'index.html', context)


class IdeasListView(ListView):
    model = Idea
    template_name = 'ideas/list.html'
    # paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ideas'] = Idea.objects.all()
        context['category'] = Category.objects.all()
        return context



class IdeasDetailView(DetailView):
    model = Idea
    template_name = 'ideas/idea_detail.html'

    def check_like(self):
        idea = self.get_object()
        if idea.likes_set.all().count() == 0:
            return f'No likes yet'
        else:
            likers = []
            for like in idea.likes_set.all():
                likers.append(like.author.username)
            result = ', '.join(likers)
        return f'Liked: {result}'

    def check_dislike(self):
        idea = self.get_object()
        if idea.dislikes_set.all().count() == 0:
            return f'No dislikes. Great!'
        else:
            dislikers = []
            for dislike in idea.dislikes_set.all():
                dislikers.append(dislike.author.username)
            result = ', '.join(dislikers)
        return f'Disliked: {result}'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['check_like'] = self.check_like()
        context['check_dislike'] = self.check_dislike()
        return context

class IdeasCreateView(GroupRequiredMixin, CreateView):
    model = Idea
    form_class = IdeasForm
    template_name = 'ideas/idea_form.html'
    group_name = ["User"]

    def get_success_url(self):
        return reverse_lazy('ideas:detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)




class IdeasUpdateView(GroupRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Idea
    fields = '__all__'
    template_name = 'ideas/idea_update_form.html'
    group_name = ["User"]

    def get_success_url(self):
        return reverse_lazy('ideas:detail', kwargs={'pk': self.object.pk})

    def test_func(self):
        return self.author_or_staff_permission()

    def author_or_staff_permission(self):
        idea = get_object_or_404(Idea, pk=self.kwargs['pk'])
        return self.request.user.is_staff or idea.author == self.request.user

class IdeasDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Idea
    success_url = reverse_lazy('ideas:list')
    template_name = 'ideas/idea_confirm_delete.html'

    def test_func(self):
        return self.author_or_staff_permission()

    def author_or_staff_permission(self):
        idea = get_object_or_404(Idea, pk=self.kwargs['pk'])
        return self.request.user.is_staff or idea.author == self.request.user


class AddLike(View):
    def get(self, request, pk):
        user = request.user
        if user.is_authenticated:
            if Likes.objects.filter(idea_id=pk, author=user).exists():
                like = Likes.objects.get(idea_id=pk, author=user)
                like.delete()
                return redirect(reverse('ideas:detail', kwargs={'pk': pk}))
            else:
                try:
                    dislike = DisLikes.objects.filter(idea_id=pk, author=user)
                    dislike.delete()

                    new_like = Likes()
                    new_like.author = request.user
                    new_like.idea_id = int(pk)
                    new_like.save()
                    return redirect(reverse('ideas:detail', kwargs={'pk': pk}))

                except:
                    new_like = Likes()
                    new_like.author = request.user
                    new_like.idea_id = int(pk)
                    new_like.save()
                    return redirect(reverse('ideas:detail', kwargs={'pk': pk}))
        else:
            return redirect(reverse('users:login'))


class DisLike(View):
    def get(self, request, pk):
        user = request.user
        if user.is_authenticated:
            if DisLikes.objects.filter(idea_id=pk, author=user).exists():
                dislike = DisLikes.objects.get(idea_id=pk, author=user)
                dislike.delete()
                return redirect(reverse('ideas:detail', kwargs={'pk': pk}))
            else:
                try:
                    like = Likes.objects.get(idea_id=pk, author=user)
                    like.delete()

                    new_dislike = DisLikes()
                    new_dislike.author = request.user
                    new_dislike.idea_id = int(pk)
                    new_dislike.save()
                    return redirect(reverse('ideas:detail', kwargs={'pk': pk}))

                except:
                    new_dislike = DisLikes()
                    new_dislike.author = request.user
                    new_dislike.idea_id = int(pk)
                    new_dislike.save()
                return redirect(reverse('ideas:detail', kwargs={'pk': pk}))
        else:
            return redirect(reverse('users:login'))


class IdeasFilter(FilterView):
    model = Idea
    template_name = 'ideas/list.html'
    filterset_class = IdeaFilter