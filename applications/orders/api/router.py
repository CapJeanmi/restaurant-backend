from rest_framework.routers import DefaultRouter
from .views import OrderApiViewSet


router_orders = DefaultRouter()
router_orders.register(prefix='orders', viewset=OrderApiViewSet, basename='orders')
