from rest_framework import serializers

from banksy.models import Bank

# Serializers define the API representation.
class BankSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bank
        fields = ('ifsc', 'bank_name', 'branch', 'address', 'city', 'district', 'state')