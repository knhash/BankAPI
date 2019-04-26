from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from bankapi.serializers import BankSerializer
from banksy.models import Bank

# Create your views here.

# ViewSets define the view behavior.
class BankViewSet(viewsets.ModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

    def get_queryset(self):
        ifsc = self.request.query_params.get('ifsc')
        city = self.request.query_params.get('city')
        bank_name = self.request.query_params.get('bank_name')
        if city and bank_name:
            queryset = Bank.objects.all().filter(city=city, bank_name=bank_name)
        elif ifsc:
            queryset = Bank.objects.all().filter(ifsc=ifsc)
        else:
            queryset = Bank.objects.all()
        return queryset
