from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from category.models import Category
from comment.forms import CommentForm
from comment.models import Comment
from .models import Idea
from .forms import IdeasForm
from user.group_permission import GroupRequiredMixin


def index(request):
    ideas = Idea.objects.all()
    categories = Category.objects.all()
    return render(request, 'index.html', {'ideas': ideas, 'categories': categories})

def ideas_list_view(request):

    ideas = Idea.objects.select_related("category").select_related("author").all()
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
    group_name = "User"

    def get_success_url(self):
        return reverse_lazy('ideas:detail', kwargs={'pk': self.object.pk})



class IdeasUpdateView(GroupRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Idea
    fields = '__all__'
    template_name = 'ideas/idea_update_form.html'
    group_name = "User"

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
