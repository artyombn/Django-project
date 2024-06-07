from django.shortcuts import render
from .models import Comment


def comments_list_view(request):

    comments = Comment.objects.all()
    return render(request, "comment/list.html", {"comments": comments})
