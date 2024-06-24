from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from idea.models import Idea
from .forms import CommentForm
from .models import Comment
from user.group_permission import GroupRequiredMixin


class BaseCommentView(GroupRequiredMixin):
    model = Comment
    group_name = "User"

    def get_success_url(self):
        idea = self.object.idea
        return reverse(
            "ideas:detail",
            kwargs={"pk": idea.pk},
        )

def comments_list_view(request):

    comments = Comment.objects.all()
    return render(request, "comment/list.html", {"comments": comments})

class CommentListView(ListView):
    model = Comment
    template_name = 'comment/list.html'
    # paginate_by = 10


class CommentDetailView(LoginRequiredMixin, DetailView):
    model = Comment
    template_name = 'comment/comment_detail.html'

class CommentCreateView(BaseCommentView, CreateView):
    form_class = CommentForm
    # template_name = 'comment/comment_form.html'

    def form_valid(self, form):
        print('Form valid')
        form.instance.author = self.request.user
        form.instance.idea = get_object_or_404(Idea, pk=self.kwargs.get("pk"))
        return super().form_valid(form)

    def get_success_url(self):
        print('get_success done')
        return reverse_lazy('comment:detail', kwargs={'pk': self.object.pk})


class CommentUpdateView(BaseCommentView, UserPassesTestMixin, UpdateView):
    form_class = CommentForm
    template_name = 'comment/comment_update_form.html'

    def get_object(self, queryset=None):
        comment = super().get_object(queryset)
        self.comment = comment
        return comment

    def get_success_url(self):
        return reverse_lazy('ideas:detail', kwargs={'pk': self.comment.idea.pk})
        # return reverse_lazy('comment:detail', kwargs={'pk': self.object.pk})

    def test_func(self):
        return self.author_or_staff_permission()

    def author_or_staff_permission(self):
        comment = get_object_or_404(Comment, pk=self.kwargs['pk'])
        return self.request.user.is_staff or comment.author == self.request.user

class CommentDeleteView(BaseCommentView, UserPassesTestMixin, DeleteView):
    template_name = 'comment/comment_confirm_delete.html'

    def get_object(self, queryset=None):
        comment = super().get_object(queryset)
        self.comment = comment
        return comment

    def get_success_url(self):
        return reverse_lazy('ideas:detail', kwargs={'pk': self.comment.idea.pk})


    def test_func(self):
        return self.author_or_staff_permission()

    def author_or_staff_permission(self):
        comment = get_object_or_404(Comment, pk=self.kwargs['pk'])
        return self.request.user.is_staff or comment.author == self.request.user
