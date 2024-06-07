from django.shortcuts import render
from .models import User


def users_list_view(request):

    users = User.objects.all()
    return render(request, "user/list.html", {"users": users})