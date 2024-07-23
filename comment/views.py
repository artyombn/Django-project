from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from django.views.generic.base import View

from idea.models import Idea
from .forms import CommentForm
from .models import Comment, CommentLikes
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

    def check_comment_like(self):
        comment = self.get_object()
        if comment.commentlikes_set.all().count() == 0:
            return f'No likes yet'
        else:
            comment_likers = []
            for comment in comment.commentlikes_set.all():
                comment_likers.append(comment)
            result = ', '.join(comment_likers)
        return f'Liked: {result}'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['check_comment_like'] = self.check_comment_like()
        return context

class CommentCreateView(GroupRequiredMixin, CreateView):
    form_class = CommentForm
    group_name = ["User"]
    # template_name = 'comment/comment_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.idea = get_object_or_404(Idea, pk=self.kwargs.get("pk"))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('comment:detail', kwargs={'pk': self.object.pk})


class CommentUpdateView(UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comment/comment_update_form.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        comment = self.get_object()
        data = json.loads(request.body)
        comment.text = data.get('text', comment.text)
        comment.save()
        return JsonResponse({'text': comment.text})

    def get_object(self, queryset=None):
        comment = super().get_object(queryset)
        self.comment = comment
        return comment

    def get_success_url(self):
        return reverse_lazy('ideas:detail', kwargs={'pk': self.comment.idea.pk})

    def test_func(self):
        comment = self.get_object()
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



class CommentLike(View):

    def get(self, request, pk):
        user = request.user
        if user.is_authenticated:
            if CommentLikes.objects.filter(comment_id=pk, author=user).exists():
                comment = Comment.objects.get(pk=pk)
                idea_id = comment.idea.id
                like = CommentLikes.objects.get(comment_id=pk, author=user)
                like.delete()
                return redirect(reverse('ideas:detail', kwargs={'pk': idea_id}))
            else:
                comment = Comment.objects.get(pk=pk)
                new_like = CommentLikes()
                new_like.author = request.user
                new_like.comment = comment
                new_like.save()
                idea_id = comment.idea.id
                return redirect(reverse('ideas:detail', kwargs={'pk': idea_id}))
        else:
            return redirect(reverse('users:login'))