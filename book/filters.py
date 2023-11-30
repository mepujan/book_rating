import django_filters
from .models import Book


class PublicationRangeFiltering(django_filters.FilterSet):
    publication_date = django_filters.DateFromToRangeFilter()

    class Meta:
        model = Book
        fields = ['author', 'publication_date']
