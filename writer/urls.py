from django.urls import path, include
from rest_framework.routers import DefaultRouter

from writer.views import WriterViewSet

router = DefaultRouter()
router.register(r'', WriterViewSet)

urlpatterns = [
    path('', include(router.urls)),
]