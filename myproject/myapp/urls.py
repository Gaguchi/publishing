from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ImageUploadViewSet, TemplateViewSet, generate_pdf

router = DefaultRouter()
router.register(r'images', ImageUploadViewSet)
router.register(r'templates', TemplateViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/generate-pdf/', generate_pdf),
]