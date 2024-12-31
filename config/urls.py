from django.contrib import admin
from django.urls import path, include
from books.views import book_list, book_update

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('books.urls')),
    path('', book_list, name='book_list'),
    path('update/<int:id>/', book_update, name='book_update'),
]
