from rest_framework.routers import DefaultRouter
from .views import ProductApiViewSet


router_product = DefaultRouter()
router_product.register(
    prefix='products', 
    viewset=ProductApiViewSet, 
    basename='products')
