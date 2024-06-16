from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import CommentForm

from .models import Comment


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

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comment/comment_form.html'

    def get_success_url(self):
        return reverse_lazy('comment:detail', kwargs={'pk': self.object.pk})


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    fields = '__all__'
    template_name = 'comment/comment_update_form.html'

    def get_success_url(self):
        return reverse_lazy('comment:detail', kwargs={'pk': self.object.pk})

    def test_func(self):
        return self.author_or_staff_permission()

    def author_or_staff_permission(self):
        comment = get_object_or_404(Comment, pk=self.kwargs['pk'])
        return self.request.user.is_staff or comment.author == self.request.user

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    success_url = reverse_lazy('comment:list')
    template_name = 'comment/comment_confirm_delete.html'

    def test_func(self):
        return self.author_or_staff_permission()

    def author_or_staff_permission(self):
        comment = get_object_or_404(Comment, pk=self.kwargs['pk'])
        return self.request.user.is_staff or comment.author == self.request.user
