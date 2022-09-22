import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"

'''
def encode():
    model = ClientModel('2424293', 79184738776, 918, 'cl', '2')
    model_sr = ClientSerializer(model)
    print(model_sr.data, type(model_sr.data), sep='\n')
    json = JSONRenderer().render(model_sr.data)
    print(json)

def decode():
    stream = io.BytesIO(b'{"client_id":"2424293","client_phone":79184738776,"client_op":918,"client_tag":"cl","client_zone":"2"}')
    data = JSONParser().parse(stream)
    serializer = ClientSerializer(data=data)
    serializer.is_valid()
    print(serializer.validated_data)
    
class ClientModel:
    def __init__(self, client_id, client_phone, client_op, client_tag, client_zone):
       self.client_id = client_id
       self.client_phone = client_phone
       self.client_op = client_op
       self.client_tag = client_tag
       self.client_zone = client_zone

    '''