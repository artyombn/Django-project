from django.contrib.auth import login
from django.test import TestCase
from django.urls import reverse

from idea.models import Idea
from user.models import User
from category.models import Category


class TestCategoryListView(TestCase):

    def setUp(self):
        self.url = '/list/'

    def test_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)



class TestCategoryDetailView(TestCase):

    def setUp(self):

        self.username = 'user'
        self.password = 'user'

        self.user = User.objects.create_user(username=self.username, password=self.password)
        self.category = Category.objects.create(title='Category1')
        self.url = reverse('category:detail', kwargs={'pk': self.category.pk})

    def test_status_code(self):
        self.client.force_login(self.user)
        # self.client.login(username=self.username, password=self.password)

        self.assertTrue(login)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        # self.assertRedirects(
        #     response,
        #     '/login/',
        #     200,
        # )

        self.client.logout()

    def test_context(self):
        self.client.force_login(self.user)
        response = self.client.get(self.url)
        self.assertIn('ideas', response.context)

        self.client.logout()


class TestCategoryCreateView(TestCase):

    def setUp(self):

        self.category = Category.objects.create(title='Category1')
        self.url = reverse('category:create')

    def test_status_code_with_no_permission(self):
        self.user = User.objects.create_user(username='user', password='user')
        self.client.force_login(self.user)
        self.assertTrue(login)

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 403)
        self.assertTemplateUsed(response, 'components/403_forbidden_splash.html')

        self.client.logout()

    def test_status_code_with_permission(self):
        self.user = User.objects.create_user(username='admin', password='admin', is_staff=True)
        self.client.force_login(self.user)
        self.assertTrue(login)

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('category/category_form.html')

        self.client.logout()

    def test_create_category(self):
        self.user = User.objects.create_user(username='admin', password='admin', is_staff=True)
        self.client.force_login(self.user)
        self.assertTrue(login)

        data = {
            'title': 'Category2',
            'description': 'Test CategoryCreateView',
        }

        response_filled_form = self.client.post(self.url, data)
        self.assertEqual(response_filled_form.status_code, 302)
        self.assertTemplateUsed('category/category_detail.html')

        category2 = Category.objects.get(title='Category2')
        self.assertIn(category2, Category.objects.all())

        expected_url = reverse('category:detail', kwargs={'pk':category2.pk})
        self.assertRedirects(response_filled_form, expected_url)

        self.client.logout()


class TestCategoryUpdateView(TestCase):

    def setUp(self):
        self.category = Category.objects.create(title='Category3', description='Category3 before updating')
        self.url = reverse('category:update', kwargs={'pk': self.category.pk})

    def test_status_code_with_no_permission(self):
        self.user = User.objects.create_user(username='user', password='user')
        self.client.force_login(self.user)
        self.assertTrue(login)

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 403)
        self.assertTemplateUsed(response, 'components/403_forbidden_splash.html')

        self.client.logout()

    def test_status_code_with_permission(self):
        self.user = User.objects.create_user(username='admin', password='admin', is_staff=True)
        self.client.force_login(self.user)
        self.assertTrue(login)

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'category/category_update_form.html')

        self.client.logout()

    def test_update_category(self):
        self.user = User.objects.create_user(username='admin', password='admin', is_staff=True)
        self.client.force_login(self.user)
        self.assertTrue(login)

        data = {
            'title': 'Updated_Category3',
            'description': 'Test View Update Category',
        }

        response_filled_update_form = self.client.post(self.url, data)
        self.assertEqual(response_filled_update_form.status_code, 302)
        self.assertTemplateUsed('category/category_detail.html')

        category3 = Category.objects.get(pk=self.category.pk)
        self.assertEqual(category3.title, 'Updated_Category3')
        self.assertEqual(category3.description, 'Test View Update Category')

        expected_url = reverse('category:detail', kwargs={'pk': category3.pk})
        self.assertRedirects(response_filled_update_form, expected_url)

        self.client.logout()



class TestCategoryDeleteView(TestCase):

    def setUp(self):
        self.category = Category.objects.create(title='CategoryDelete', description='Category before removal')
        self.url = reverse('category:delete', kwargs={'pk': self.category.pk})

    def test_status_code_with_no_permission(self):
        self.user = User.objects.create_user(username='user', password='user')
        self.client.force_login(self.user)
        self.assertTrue(login)

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 403)
        self.assertTemplateUsed(response, 'components/403_forbidden_splash.html')

        self.client.logout()

    def test_status_code_with_permission(self):
        self.user = User.objects.create_user(username='admin', password='admin', is_staff=True)
        self.client.force_login(self.user)
        self.assertTrue(login)

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'category/category_confirm_delete.html')

        self.client.logout()

    def test_delete_category(self):
        self.user = User.objects.create_user(username='admin', password='admin', is_staff=True)
        self.client.force_login(self.user)
        self.assertTrue(login)

        category_delete = Category.objects.get(title='CategoryDelete')
        self.assertIn(category_delete, Category.objects.all())

        response_delete_form = self.client.delete(self.url, kwargs={'pk': category_delete.pk})
        self.assertEqual(response_delete_form.status_code, 302)
        self.assertTemplateUsed('category/list.html')

        self.assertNotIn(category_delete, Category.objects.all())

        self.client.logout()