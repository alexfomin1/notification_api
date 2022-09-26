from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from tags.models import Tag
from tags.serializers import TagSerializer


# Create your views here.
class TagsViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (IsAuthenticated,)