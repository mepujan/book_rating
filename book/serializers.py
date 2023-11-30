from rest_framework import serializers
from .models import Book, Rating


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'author',
                  'publication_date', 'isbn', 'rating')


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = "__all__"
