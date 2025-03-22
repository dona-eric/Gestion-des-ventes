from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, SaleViewSet, UserViewSet, ReturnViewSet, get_facture
#from django.urls import path, re_path
from rest_framework import permissions
#from drf_yasg.views import get_schema_view
#from drf_yasg import openapi
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'products', ProductViewSet, basename="product")
router.register(r'sales', SaleViewSet, basename='sale')
router.register(r'returns', ReturnViewSet, basename="return")


"""schema_view = get_schema_view(
    openapi.Info(
        title="API de Gestion des Ventes",
        default_version='v1',
        description="Documentation de l'API pour l'application de gestion des ventes",
        terms_of_service="https://www.ton-site.com/terms/",
        contact=openapi.Contact(email="support@ton-site.com"),
        license=openapi.License(name="Licence MIT"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)"""
urlpatterns = [
    path('api/', include(router.urls)),
    path('sales/<int:sale_id>/facture/', get_facture, name='facture'),
    path('sales/<int:pk>/update_payment/', SaleViewSet.as_view({'put':'update_payment_status'}),name='update_payment'),
    path('sales/<int:pk>/make_payment/', SaleViewSet.as_view({'put':'make_payment'}), name='make_payment'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   # path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    #path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    #re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]



