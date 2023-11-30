from rest_framework.routers import DefaultRouter
from .views import BookViewSet, RatingViewSet

router = DefaultRouter()
router.register(r'book', BookViewSet, basename='book')
router.register(r'ratings', RatingViewSet, basename='ratings')

urlpatterns = router.urls
