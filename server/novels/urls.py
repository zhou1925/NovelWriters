from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NovelViewSet

app_name = 'novels'

router = DefaultRouter()
router.register('', NovelViewSet)


urlpatterns = [
    path('', include(router.urls))
]
