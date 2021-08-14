from rest_framework import routers

from api import views


router = routers.DefaultRouter()
router.register(r'customer', views.CustomerViewSet)
router.register(r'wishlist', views.WishListViewSet)
router.register(r'product', views.ProductViewSet)
router.register(r'user', views.UserViewSet)
