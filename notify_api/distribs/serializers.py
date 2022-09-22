from rest_framework import serializers

from distribs.models import Distrib


class DistribSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distrib
        fields = "__all__"