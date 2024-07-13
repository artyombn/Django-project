import django_filters
from .models import Idea


class IdeaFilter(django_filters.FilterSet):
    class Meta:
        model = Idea
        fields = {
            'category': ['exact'],
            'status': ['exact'],
            'created_at': ['date', 'year__gte', 'year__lte'],
        }