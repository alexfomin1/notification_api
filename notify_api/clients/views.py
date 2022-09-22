from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Client
from .serializers import ClientSerializer


class ClientsAPIView(APIView):
    def get(self, request):
        lst = Client.objects.all().values()
        return Response({'posts': ClientSerializer(lst, many=True).data})

    def post(self, request):
        serializer = ClientSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})

#class ClientsAPIView(generics.ListAPIView):
#    queryset = Client.objects.all()
#    serializer_class = ClientSerializer