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

        post_new = Client.objects.create(
            client_id=request.data['client_id'],
            client_phone=request.data['client_phone'],
            client_op=request.data['client_op'],
            client_tag=request.data['client_tag'],
            client_zone=request.data['client_zone']
        )
        return Response({'post': ClientSerializer(post_new).data})

#class ClientsAPIView(generics.ListAPIView):
#    queryset = Client.objects.all()
#    serializer_class = ClientSerializer