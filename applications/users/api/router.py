from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserApiViewSet, UserView
from rest_framework_simplejwt.views import TokenObtainPairView

router_user = DefaultRouter()
router_user.register(prefix='users', viewset=UserApiViewSet, basename='users')

app_name = 'api'
urlpatterns = [
    path('auth/me/', UserView.as_view(), name='users'),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair')
]