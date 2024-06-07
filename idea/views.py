from django.shortcuts import render
from .models import Idea

# Create your views here.

def ideas_list_view(request):

    ideas = Idea.objects.all()
    return render(request, 'ideas/list.html', {'ideas': ideas})