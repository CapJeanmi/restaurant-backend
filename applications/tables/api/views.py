from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import TableSerializer
from ..models import Table


class TableViewSet(ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = TableSerializer
    queryset = Table.objects.all().order_by('number')
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['number']
    