from rest_framework import serializers
from .models import InvoiceDetails, Unit




class InvoiceDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceDetails
        fields = "__all__"


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = "__all__"


