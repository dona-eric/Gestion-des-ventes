from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .models import Sale, Product, User
from .serializers import SaleSerializer, UserSerializer, ProductSerializer

## we wanted combine the  des users, sales and products
# Permission to restrict
class IsOwner(permissions.BasePermission):
    """aux admins de modifier les stocks"""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'owner'

class IsEmployee(permissions.BasePermission):
    """aux employées de voir les products et register des sales"""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'employee'

"""The views to manage the users , products and sales model's
this method cover all possible actions(create, read, update, delete)CRUD.
you can use ModelViewSet instead of ReadOnlyViewSet """
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsOwner]  # only the admin(owner) can manage the users

# manage the products
class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    """
    - employee : can only see their products who available in
    - Admin : can see all things and modify if possible
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

# manage of sales
class SaleViewSet(viewsets.ModelViewSet):
    serializer_class = SaleSerializer
    queryset = Sale.objects.all()
    def get_queryset(self):
        """only the admin can see all things(sales saved and others things)
        but the employee could see this sales saved"""
        user = self.request.user
        if user.role == 'owner':
            return Sale.objects.all()
        return Sale.objects.filter(employee=user)

    def perform_create(self, serializer):
        """ the non owner register the sales saved in his/her names"""
        serializer.save(employee=self.request.user)

    def destroy(self, request, *args, **kwargs):
        """only owner can delete a sales"""
        if request.user.role != 'owner':
            return Response({"error": "Only the owner(admin) has the all permissions to delete the sales"}, status=403)
        return super().destroy(request, *args, **kwargs)