from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from idea.models import Idea
from .models import Category
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import CategoryForm
from user.group_permission import GroupRequiredMixin


def category_list_view(request):

    categories = Category.objects.all()
    return render(request, "category/list.html", {"categories": categories})


class CategoryListView(ListView):
    model = Category
    template_name = 'category/list.html'

class CategoryDetailView(GroupRequiredMixin, DetailView):
    model = Category
    template_name = 'category/category_detail.html'
    group_name = "User"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ideas'] = Idea.objects.filter(category=self.object)
        return context

class CategoryCreateView(GroupRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/category_form.html'
    group_name = ["Verified", "Mods", "Admin"]

    def get_success_url(self):
        return reverse_lazy('category:detail', kwargs={'pk': self.object.pk})


class CategoryUpdateView(GroupRequiredMixin, UpdateView):
    model = Category
    fields = '__all__'
    template_name = 'category/category_update_form.html'
    group_name = ["Verified", "Mods", "Admin"]

    def get_success_url(self):
        return reverse_lazy('category:detail', kwargs={'pk': self.object.pk})


class CategoryDeleteView(GroupRequiredMixin, DeleteView):
    model = Category
    success_url = reverse_lazy('category:list')
    template_name = 'category/category_confirm_delete.html'
    group_name = ["Verified", "Mods", "Admin"]