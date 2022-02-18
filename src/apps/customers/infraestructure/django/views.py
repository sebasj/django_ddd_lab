from rest_framework.views import APIView
from rest_framework.response import Response


from customers.application.customers_use_cases import CustomersListUseCase

from customers.infraestructure.django.serializers import CustomerSerializer
from customers.infraestructure.django.repositories import CustomerDjangoRepository



class CustomersListAPIView(APIView):
    def get(self, request, format=None):
        customers = CustomersListUseCase(customers_repository=CustomerDjangoRepository())
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)