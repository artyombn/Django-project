from django.core.management.base import BaseCommand
from category.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):

        Category.objects.all().delete()

        print("Filling db ...")

        categories = [
            Category(title="Tech", description="Startups and technology projects including AI, software and blockchain"),
            Category(title="Society", description="Social aspects of life such as education and health"),
            Category(title="Creative", description="Art, design, music and movie etc"),
        ]

        Category.objects.bulk_create(categories)

        print("Done")

        print(Category.objects.all())