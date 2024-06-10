from django.shortcuts import render
from .models import Idea

# Create your views here.

def ideas_list_view(request):

    ideas = Idea.objects.select_related("category").select_related("author").all()
    return render(request, 'ideas/list.html', {'ideas': ideas})