from rest_framework import serializers
from api.models import Transfer

class TransferSerializers(serializers.ModelSerializer):
    class Meta:
        model = Transfer
        fields = ['hbl', 'name', 'city', 'state']