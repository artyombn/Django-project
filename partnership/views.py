from django.shortcuts import render
from django.views.generic import ListView
from partnership.models import CoAuthor


class CoAuthorsView(ListView):
    model = CoAuthor
    template_name = 'partnership/coauthors.html'

