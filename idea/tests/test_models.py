from django.test import TestCase
from idea.models import Idea
from category.models import Category
from user.models import User
from comment.models import Comment

class TestIdea(TestCase):

    def setUp(self):
        print('Implementation before test starts')

        self.category = Category.objects.create(
            title='FinTech'
        )

        self.author = User.objects.create(
            username='artyombn',
            email='artyombn@gmail.com'
        )

        self.idea = Idea.objects.create(
            title='Idea1',
            category=self.category,
            author=self.author
        )

    def tearDown(self):
        print('Implementation after each test')


    def test_str(self):
        self.assertEqual(str(self.idea), f'Idea1/FinTech/artyombn')


    def test_comments_count(self):

        for i in range(5):
            Comment.objects.create(
                idea=self.idea,
                author=self.author,
                text="Comment1"
            )

        self.assertEqual(self.idea.comments_count(), 5)