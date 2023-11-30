from django.db import models
from django.contrib.auth.models import User
from math import ceil


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, models.CASCADE)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.author.username} has created book {self.title}"

    class Meta:
        ordering = ('-created',)

    def rating(self):
        result = self.ratings.aggregate(models.Avg('rating'))
        if result.get('rating__avg') is None:
            result['rating__avg'] = 0
        return ceil(result['rating__avg'])


class Rating(models.Model):
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    review = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.user.username} has rated book {self.book.title}"
