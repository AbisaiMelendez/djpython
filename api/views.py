#from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import CertificateSerializer, DomainSerializer
from .models import Certificate, Domain



class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer

class DomainViewSet(viewsets.ModelViewSet):
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer
