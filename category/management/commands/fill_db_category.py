from django.core.management.base import BaseCommand
from category.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):

        Category.objects.all().delete()

        print("Filling db Category...")

        categories = [
            Category(title="Technology",
                     description="Innovative projects in AI, software development, and blockchain technology",
                     image='/category_images/technology.png'),
            Category(title="Society",
                     description="Social aspects of life including education and healthcare initiatives",
                     image='/category_images/society.png'),
            Category(title="Creative",
                     description="Art, design, music, and film projects fostering creativity and innovation",
                     image='/category_images/design_exchange.jpeg'),
            Category(title="Health",
                     description="Projects focused on improving health outcomes and medical innovations",
                     image='/category_images/healthcare.jpg'),
            Category(title="Finance",
                     description="Financial technology (Fintech), startups, and economic ventures",
                     image='/category_images/finance.jpg'),
            Category(title="Education",
                     description="Projects and initiatives focused on innovative education methods and lifelong learning",
                     image='/category_images/education.jpg'),
        ]

        Category.objects.bulk_create(categories)

        print("Done")

        print(Category.objects.all())