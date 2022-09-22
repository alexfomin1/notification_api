from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly


from .models import Client
from .serializers import ClientSerializer

class ClientsViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

