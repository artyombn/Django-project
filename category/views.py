from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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

class CategoryDetailView(LoginRequiredMixin, DetailView):
    model = Category
    template_name = 'category/category_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ideas'] = Idea.objects.filter(category=self.object)
        return context

class CategoryCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/category_form.html'

    def get_success_url(self):
        return reverse_lazy('category:detail', kwargs={'pk': self.object.pk})

    def test_func(self):
        return self.only_staff_permission()

    def only_staff_permission(self):
        user = self.request.user
        return user.is_staff

class CategoryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Category
    fields = '__all__'
    template_name = 'category/category_update_form.html'

    def get_success_url(self):
        return reverse_lazy('category:detail', kwargs={'pk': self.object.pk})

    def test_func(self):
        return self.only_staff_permission()

    def only_staff_permission(self):
        user = self.request.user
        return user.is_staff

class CategoryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Category
    success_url = reverse_lazy('category:list')
    template_name = 'category/category_confirm_delete.html'

    def test_func(self):
        return self.only_staff_permission()

    def only_staff_permission(self):
        user = self.request.user
        return user.is_staff