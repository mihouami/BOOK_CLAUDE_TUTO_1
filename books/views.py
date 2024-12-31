from rest_framework import viewsets, filters as drf_filters
from django_filters.rest_framework import DjangoFilterBackend
from .filters import BookFilter
from .pagination import StandardResultsSetPagination
from .models import Book
from .serializers import BookSerializer
from django.shortcuts import render
from rest_framework.permissions import AllowAny



class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all() # Base queryset for all operations
    serializer_class = BookSerializer # Serializer to use for all operations
    permission_classes = [AllowAny]  # Allow everyone to access this viewset
    pagination_class = StandardResultsSetPagination  # Custom pagination class
    filter_backends = [DjangoFilterBackend, # For exact and custom filters
                       drf_filters.SearchFilter, # For search functionality
                       drf_filters.OrderingFilter, # For sorting
                       ]
    filterset_class = BookFilter  # Custom filter class
    search_fields = ['title', 'author', 'description']  # Fields to search in
    # GET /api/books/?search=hobbit  # Search in title, author, and description
    
    ordering_fields = ['title', 'author', 'published_year', 'created_at']  # Fields that can be sorted
    #GET /api/books/?ordering=title  # Order by title (ascending)
    #GET /api/books/?ordering=-published_year  # Order by year (descending)
    
    ordering = ['-created_at']  # Default ordering
    
    #COMBINE FILTERS AND ORDERING
    #GET /api/books/?search=fantasy&ordering=-published_year&page_size=20
    
    
    # ModelViewSet provides all CRUD actions:
    # list(), create(), retrieve(), update(), destroy()
    # GET - api/books/: Lists all books.
    # GET - api/books/<id>/: Retrieves a specific book.
    # POST - api/books/: Creates a new book.
    # PUT - api/books/<id>/: Updates a specific book.
    # DELETE - api/books/<id>/: Deletes a specific book.
    
    # Example of overriding a default method
    def create(self, request, *args, **kwargs):
        """
        Custom create method to add extra logic
        """
        # First, let's create the book using the default create method
        response = super().create(request, *args, **kwargs)
        
        # Add custom logic here, for example:
        print(f"New book created: {response.data['title']}")
        
        return response
    
    
def book_list(request):
    print(request)
    return render(request, 'book_list.html')

    
def book_update(request, id):
    return render(request, 'update_book.html', {'book_id': id})
    
    
'''
    # Optional: Add custom endpoints
    from rest_framework.response import Response
    from rest_framework.decorators import action
    
    
    
    # Optional: Add custom filtering
    # Add - api/books/?author=<name> to the URL to filter books by author.
    def get_queryset(self):
        
        Customize the queryset based on URL parameters.
        Example: /api/books/?author=Orwell
        
        queryset = Book.objects.all()
        # Get the 'author' parameter from URL if it exists
        author = self.request.query_params.get('author', None)
        if author:
            queryset = queryset.filter(author__icontains=author)
        return queryset
    
    # Optional: Add a custom endpoint for book search
    # GET - api/books/search/?q=<query> searches books by title or author.
    @action(detail=False, methods=['get'])
    def search(self, request):
        """
        Custom endpoint for searching books.
        URL: /api/books/search/?q=1984
        """
        query = request.query_params.get('q', None)
        books = Book.objects.filter(title__icontains=query) | Book.objects.filter(author__icontains=query)
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
'''
