from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Idea
from .forms import IdeasForm
from django.shortcuts import render, redirect


def ideas_list_view(request):

    ideas = Idea.objects.select_related("category").select_related("author").all()
    return render(request, 'ideas/list.html', {'ideas': ideas})


class IdeasListView(ListView):
    model = Idea
    template_name = 'ideas/list.html'
    paginate_by = 10
    # context_object_name = 'ideas'


class IdeasDetailView(DetailView):
    model = Idea
    template_name = 'ideas/idea_detail.html'

class IdeasCreateView(CreateView):
    model = Idea
    form_class = IdeasForm
    template_name = 'ideas/idea_form.html'

    def get_success_url(self):
        return reverse_lazy('ideas:detail', kwargs={'pk': self.object.pk})


class IdeasUpdateView(UpdateView):
    model = Idea
    fields = '__all__'
    template_name = 'ideas/idea_update_form.html'

    def get_success_url(self):
        return reverse_lazy('ideas:detail', kwargs={'pk': self.object.pk})

class IdeasDeleteView(DeleteView):
    model = Idea
    success_url = reverse_lazy('ideas:list')
    template_name = 'ideas/idea_confirm_delete.html'
