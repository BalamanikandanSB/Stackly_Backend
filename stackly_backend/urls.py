from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import ProductViewSet, OrderViewSet
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# -----------------------------
# Router
# -----------------------------
router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='products')
router.register(r'orders', OrderViewSet, basename='orders')

# -----------------------------
# Swagger schema view
# -----------------------------
schema_view = get_schema_view(
   openapi.Info(
      title="Stackly API",
      default_version='v1',
      description="API documentation for Stackly",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

# -----------------------------
# URL patterns
# -----------------------------
urlpatterns = [
    # Admin panel
    path('admin/', admin.site.urls),

    # API endpoints
    path('api/', include(router.urls)),

    # Swagger docs
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    # ReDoc docs (optional)
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
