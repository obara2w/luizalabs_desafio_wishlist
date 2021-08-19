from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import mixins
from drf_spectacular.utils import extend_schema

from api.models import Customer, Wishlist, Product
from api.serializers import UserSerializer, CustomerSerializer, CustomerSerializerWithRelatedObject, \
    WishlistSerializer, WishlistSerializerWithRelatedObject, ProductSerializer


@extend_schema(tags=['Cliente'])
class CustomerViewSet(viewsets.ModelViewSet):
    """
    Operação para gerenciamento de cliente, este operação pode ser acessado apenas por usuários autenticados
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticated, ]
    pagination_class = None

    """
    Quando a action for list ou retrieve, use um Serializer diferente que inclua o objetos
    """
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return CustomerSerializerWithRelatedObject
        return super().get_serializer_class()


@extend_schema(tags=['Lista de produto favorito'])
class WishListViewSet(viewsets.ModelViewSet):
    """
    Operação para gerenciamento de lista de produtos favoritos, este operação pode ser acessado apenas por usuários autenticados
    """
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    permission_classes = [permissions.IsAuthenticated, ]
    pagination_class = None
    
    """
    Quando a action for list ou retrieve, use um Serializer diferente que inclua os objetos
    """
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return WishlistSerializerWithRelatedObject
        return super().get_serializer_class()


@extend_schema(tags=['Produto'])
class ProductViewSet(viewsets.ModelViewSet):
    """
    Operação para gerenciamento de produtos, este operação pode ser acessado apenas por usuários autenticados
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated, ]


@extend_schema(tags=['Usuário'])
class UserViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    Operação de gerenciamento de usuários, este operação pode ser acessado apenas por superusuários (admins)
    Nota: Este Operação foi criado apenas para de cumprir o requisito de autorização, uma vez que ele só pode ser acessado por admin
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    pagination_class = None
