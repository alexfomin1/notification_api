from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Message
from .serializers import MessageSerializer


class MessagesViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticated,)
