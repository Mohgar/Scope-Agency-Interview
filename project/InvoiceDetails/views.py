from django.shortcuts import render
from .serializers import InvoiceDetailsSerializer, UnitSerializer
from .models import InvoiceDetails, Unit
from rest_framework import generics



class InvoiceDetailsListCreate(generics.ListCreateAPIView):
    queryset = InvoiceDetails.objects.all()
    serializer_class = InvoiceDetailsSerializer


class InvoiceDetailsRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = InvoiceDetails.objects.all()
    serializer_class = InvoiceDetailsSerializer


class UnitListCreate(generics.ListCreateAPIView):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer


class UnitRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Unit.objects.all()
    serializer_class = InvoiceDetailsSerializer





