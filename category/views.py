from django.shortcuts import render
from .models import Category

# Create your views here.


def category_list_view(request):

    categories = Category.objects.all()
    return render(request, "category/list.html", {"categories": categories})
