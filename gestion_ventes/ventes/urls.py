from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, SaleViewSet, UserViewSet, ReturnViewSet, get_facture
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'products', ProductViewSet, basename="product")
router.register(r'sales', SaleViewSet, basename='sale')
router.register(r'returns', ReturnViewSet, basename="return")

urlpatterns = [
    path('api/', include(router.urls)),
    path('sales/<int:sale_id>/facture/', get_facture, name='facture'),
    path('sales/<int:pk>/update_payment/', SaleViewSet.as_view({'put':'update_payment_status'}),name='update_payment'),
    path('sales/<int:pk>/make_payment/', SaleViewSet.as_view({'put':'make_payment'}), name='make_payment'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]