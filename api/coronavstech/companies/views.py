from django.shortcuts import render

from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from api.coronavstech.companies.serializers import CompanySerializer
from api.coronavstech.companies.models import Company

# Create your views here.
class CompanyViewSet(ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all().order_by("-last_update")
    pagination_class = PageNumberPagination
