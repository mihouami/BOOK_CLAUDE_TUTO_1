from rest_framework import serializers
from .models import Book
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
    # We inherit from ModelSerializer which automatically creates
    # serializer fields based on our Book model
    
    class Meta:
        model = Book # Specify which model to serialize
        #fields = '__all__'
        fields = ['id', 'title', 'author', 'description', 'published_year', 'created_at', 'updated_at'] # List the fields you want to include in your API
        read_only_fields = ['created_at', 'updated_at'] # These fields can't be modified via API


    # You could add custom fields like this:
    # average_rating = serializers.FloatField(read_only=True)
    
    
    def validate_published_year(self, value):
        if value < 0:
            raise serializers.ValidationError("Published year can't be negative")
        if value > datetime.now().year:
            raise serializers.ValidationError("Published year can't be in the future")
        return value
    

'''
# Example 1:
book = Book.objects.get(id=1)
serializer = BookSerializer(book)
json_data = serializer.data
# json_data will look like:
{
    "id": 1,
    "title": "1984",
    "author": "George Orwell",
    "description": "A dystopian novel",
    "published_year": 1949,
    "created_at": "2024-01-01T12:00:00Z",
    "updated_at": "2024-01-01T12:00:00Z"
}

# Example 2:
json_data = {
    "title": "1984",
    "author": "George Orwell",
    "description": "A dystopian novel",
    "published_year": 1949
}
serializer = BookSerializer(data=json_data)
if serializer.is_valid():
    book = serializer.save()  # Creates a new Book instance


'''