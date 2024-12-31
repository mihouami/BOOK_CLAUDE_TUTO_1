# books/pagination.py
from rest_framework.pagination import PageNumberPagination

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10  # Default number of items per page
    page_size_query_param = 'page_size'  # URL parameter to override page size
    max_page_size = 100  # Maximum items client can request per page

# How it works:
# 1. GET /api/books/  -> Returns first 10 items
# 2. GET /api/books/?page=2  -> Returns items 11-20
# 3. GET /api/books/?page_size=20  -> Returns first 20 items

# Example Response:
"""
{
    "count": 35,  # Total items in database
    "next": "http://localhost:8000/api/books/?page=2",  # URL for next page
    "previous": null,  # URL for previous page (null if on first page)
    "results": [  # Current page items
        {"id": 1, "title": "Book 1", ...},
        {"id": 2, "title": "Book 2", ...},
        ...
    ]
}
"""