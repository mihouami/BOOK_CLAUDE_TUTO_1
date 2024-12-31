# books/filters.py
from django_filters import rest_framework as filters
from .models import Book

class BookFilter(filters.FilterSet):
    # Define custom filters
    title = filters.CharFilter(lookup_expr='icontains')
    # This creates a filter that searches title containing text (case-insensitive)
    # Usage: /api/books/?title=potter

    author = filters.CharFilter(lookup_expr='icontains')
    # Similar to title filter
    # Usage: /api/books/?author=rowling

    # Range filters for published year
    published_year_min = filters.NumberFilter(
        field_name='published_year',  # Model field to filter on
        lookup_expr='gte'            # Greater than or equal to
    )
    published_year_max = filters.NumberFilter(
        field_name='published_year',  # Model field to filter on
        lookup_expr='lte'            # Less than or equal to
    )
    # Usage: /api/books/?published_year_min=1990&published_year_max=2000

    class Meta:
        model = Book
        fields = ['title', 'author', 'published_year']

# Example Queries:
"""
1. Find books by Tolkien published after 1950:
   GET /api/books/?author=tolkien&published_year_min=1950

2. Find books with 'magic' in title published between 1990-2000:
   GET /api/books/?title=magic&published_year_min=1990&published_year_max=2000
"""