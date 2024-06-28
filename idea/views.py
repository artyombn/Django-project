from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic.base import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from category.models import Category
from comment.forms import CommentForm
from .models import Idea, Likes, DisLikes
from .forms import IdeasForm
from user.group_permission import GroupRequiredMixin


def index(request):
    ideas = Idea.objects.all()
    categories = Category.objects.all()
    return render(request, 'index.html', {'ideas': ideas, 'categories': categories})

def ideas_list_view(request):

    ideas = Idea.objects.select_related("category").select_related("author").select_related("likes").all()
    return render(request, 'ideas/list.html', {'ideas': ideas})


class IdeasListView(ListView):
    model = Idea
    template_name = 'ideas/list.html'
    # paginate_by = 10
    # context_object_name = 'ideas'


class IdeasDetailView(DetailView):
    model = Idea
    template_name = 'ideas/idea_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
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