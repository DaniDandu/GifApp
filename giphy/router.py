from rest_framework.routers import DefaultRouter
from .views import GifViewset 

router = DefaultRouter()
router.register('Search-GIF', GifViewset, basename='gif')