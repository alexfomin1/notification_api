from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from distribs.models import Distrib
from distribs.serializers import DistribSerializer


class DistribsViewSet(viewsets.ModelViewSet):
    queryset = Distrib.objects.all()
    serializer_class = DistribSerializer
    permission_classes = (IsAuthenticated,)

