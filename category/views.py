from django.shortcuts import render

from idea.models import Idea
from .models import Category
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import CategoryForm

# Create your views here.


def category_list_view(request):

    categories = Category.objects.all()
    return render(request, "category/list.html", {"categories": categories})


class CategoryListView(ListView):
    model = Category
    template_name = 'category/list.html'
    paginate_by = 10

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category/category_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ideas'] = Idea.objects.filter(category=self.object)
        return context

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/category_form.html'

    def get_success_url(self):
        return reverse_lazy('category:detail', kwargs={'pk': self.object.pk})

class CategoryUpdateView(UpdateView):
    model = Category
    fields = '__all__'
    template_name = 'category/category_update_form.html'

    def get_success_url(self):
        return reverse_lazy('category:detail', kwargs={'pk': self.object.pk})

class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy('category:list')
    template_name = 'category/category_confirm_delete.html'