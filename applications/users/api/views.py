from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from ..models import User
from .serializers import UserSerializer
from django.contrib.auth.hashers import make_password


class UserApiViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        request.data['password'] = make_password(request.data['password']) # Encriptar Contraseña
        return super().create(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        password = request.data['password']

        if password:
            request.data['password'] = make_password(password)
        else:
            request.data['password'] = request.user.password

        return super().partial_update(request, *args, **kwargs) # Actualizar Contraseña de Usuario y Encriptarla


class UserView(APIView):
    """Recuperar datos del usuario que está autenticado"""
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)
