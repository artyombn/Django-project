from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from category.models import Category
from user.models import User


class TestCategory(TestCase):

    def setUp(self):
        self.category = Category.objects.create(
            title='CategoryName',
            description='Test for CategoryName'
        )

    def test_str(self):
        self.assertEqual(str(self.category.title), 'CategoryName')
        self.assertEqual(str(self.category.description), 'Test for CategoryName')

    def test_created_at(self):
        self.assertIsNotNone(self.category.created_at)
        now = timezone.now()
        self.assertAlmostEqual(self.category.created_at, now.date())

    def test_updated_at(self):

        self.assertIsNotNone(self.category.updated_at)

        self.url = reverse('category:update', kwargs={'pk': self.category.pk})

        self.user = User.objects.create_user(username='admin', password='admin', is_staff=True)
        self.client.force_login(self.user)

        data = {
            'title': 'CategoryName_Updated',
            'description': 'Test updated_time',
        }

        response_filled_update_form = self.client.post(self.url, data)
        self.assertEqual(response_filled_update_form.status_code, 302)

        now = timezone.now()

        category3 = Category.objects.get(pk=self.category.pk)
        self.assertEqual(category3.title, 'CategoryName_Updated')
        self.assertEqual(category3.description, 'Test updated_time')

        self.client.logout()

        self.assertAlmostEqual(category3.updated_at, now, delta=timezone.timedelta(seconds=10))

