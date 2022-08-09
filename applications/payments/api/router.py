from rest_framework.routers import DefaultRouter

from .views import PaymentApiViewSet

router_payments = DefaultRouter()

router_payments.register(
    prefix='payments', basename='payments', viewset=PaymentApiViewSet
)
