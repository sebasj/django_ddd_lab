from rest_framework import serializers


class CustomerSerializer(serializers.Serializer):
    name = serializers.CharField()
    phone_number = serializers.CharField()
    email = serializers.CharField()
    vat_id = serializers.CharField()
