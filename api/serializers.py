from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from api.models import Customer, Wishlist, Product


class ProductSerializer(serializers.ModelSerializer):
    """
    Produto: representa um produto.
    """
    reviewScore = serializers.FloatField(source='review_score',
                                         required=not Product._meta.get_field('review_score').blank,
                                         help_text=Product._meta.get_field('review_score').help_text)

    class Meta:
        model = Product
        fields = ['id', 'title', 'brand', 'price', 'image', 'reviewScore', 'url']


class CustomerSerializer(serializers.ModelSerializer):
    """
    Cliente: representa um cliente.
    """
    class Meta:
        model = Customer
        fields = ['id', 'name', 'email']


class CustomerSerializerWithRelatedObject(CustomerSerializer):
    """
    Cliente: representa um cliente com a sua lista de produtos favoritos.
    """
    wishList = ProductSerializer(source='wish_list', many=True, required=False)

    class Meta:
        model = Customer
        fields = ['id', 'name', 'email', 'wishList']


class WishlistSerializer(serializers.ModelSerializer):
    """
    Produto favorito: representa a atribuição de um produto favorito a um cliente.
    """
    class Meta:
        model = Wishlist
        fields = ['id', 'customer', 'product']

        # Customiza mensagem de erro para o UniqueTogether
        validators = [
            UniqueTogetherValidator(
                queryset=Wishlist.objects.all(), 
                fields=('customer', 'product'),
                message='O cliente já possui esse produto incluído em sua lista de favoritos.'
            )
        ]


class WishlistSerializerWithRelatedObject(WishlistSerializer):
    """
    Produto favorito: representa a atribuição de um produto favorito a um cliente, 
    com os objetos do produto e cliente.
    """
    customer = CustomerSerializer()
    product = ProductSerializer()


class UserSerializer(serializers.ModelSerializer):
    """
    Cliente: representa um usuário.
    """
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
