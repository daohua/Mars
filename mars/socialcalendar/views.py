import django_filters
from .models import Caldata
from django.shortcuts import render
from rest_framework import generics, filters
from rest_framework.response import Response
from .serializers import CaldataSerializer

class CaldataFilter(django_filters.FilterSet):
    class Meta:
        model=Caldata
        fields = ['site', 'month']

# Create your views here.
class CaldataView(generics.ListAPIView):
    queryset = Caldata.objects.all()
    serializer_class = CaldataSerializer
    filter_backends = ( filters.DjangoFilterBackend, )
    filter_class = CaldataFilter

    # def get_queryset(self):
    #     site = self.request.GET.get('site'):
    #     month = self.request.GET.get('month')

    #     return Caldata.objects.filter(site=site,month=month)
        # if self.request.GET.get():
        #     pass
    # def get_queryset(self):
    #     return Caldata.objects.filter(site=self.kwargs['site'])

    # def get_paginate_by(self):
    #     return 20