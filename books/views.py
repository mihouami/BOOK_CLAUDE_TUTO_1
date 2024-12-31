from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Book
from .serializers import BookSerializer
from django.shortcuts import render
from rest_framework.permissions import AllowAny


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all() # Base queryset for all operations
    serializer_class = BookSerializer # Serializer to use for all operations
    permission_classes = [AllowAny]  # Allow everyone to access this viewset
    # ModelViewSet provides all CRUD actions:
    # list(), create(), retrieve(), update(), destroy()
    # GET - api/books/: Lists all books.
    # GET - api/books/<id>/: Retrieves a specific book.
    # POST - api/books/: Creates a new book.
    # PUT - api/books/<id>/: Updates a specific book.
    # DELETE - api/books/<id>/: Deletes a specific book.
    
    
    # Optional: Add custom filtering
    # Add - api/books/?author=<name> to the URL to filter books by author.
    def get_queryset(self):
        '''
        Customize the queryset based on URL parameters.
        Example: /api/books/?author=Orwell
        '''
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
    


'''
GET /api/books/ → list() → Lists all books
GET /api/books/{id}/ → retrieve() → Gets one book
GET /api/books/search/ → search() → Custom search endpoint
POST /api/books/ → create() → Creates a new book
PUT /api/books/{id}/ → update() → Updates a book
DELETE /api/books/{id}/ → destroy() → Deletes a book
'''

def book_list(request):
    return render(request, 'book_list.html')

def book_update(request, id):
    return render(request, 'update_book.html', {'book_id': id})