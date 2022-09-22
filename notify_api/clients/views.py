from django.shortcuts import render
from rest_framework import generics

from .models import Client
from .serializers import ClientSerializer


# Create your views here.
class ClientsAPIView(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer