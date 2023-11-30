from rest_framework.viewsets import ModelViewSet
from .models import Book, Rating
from .serializers import BookSerializer, RatingSerializer
from .pagination import BookPagePagination
from .filters import PublicationRangeFiltering
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.exceptions import PermissionDenied
from django_filters.rest_framework import DjangoFilterBackend


class BookViewSet(ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    pagination_class = BookPagePagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = PublicationRangeFiltering

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise PermissionDenied("User not authorized to update content")
        serializer.save()

    def perform_destroy(self, instance):
        if instance.author == self.request.user:
            instance.delete()
        raise PermissionDenied("User not authorized to delete content")

    def get_permissions(self):
        if self.action == 'destroy':
            return [IsAdminUser(),]
        return super().get_permissions()


class RatingViewSet(ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = RatingSerializer

    def get_queryset(self):
        return Rating.objects.filter(user=self.request.user)
