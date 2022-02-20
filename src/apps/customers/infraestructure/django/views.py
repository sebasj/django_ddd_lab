from rest_framework.views import APIView
from rest_framework.response import Response


from customers.application import customers_use_cases 

from customers.infraestructure.django.repositories import CustomerDjangoRepository
from customers.infraestructure.django.serializers import CustomerSerializer


class CustomersListAPIView(APIView):
    def get(self, request, format=None):
        use_case = customers_use_cases.CustomersListUseCase(customers_repository=CustomerDjangoRepository())
        customers = use_case.execute()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)


class CustomersCreateAPIView(APIView):
    def post(self, request, format=None):
        use_case = customers_use_cases.CustomerCreateUseCase(customers_repository=CustomerDjangoRepository())
        serializer = CustomerSerializer(data=request.POST)
        serializer.is_valid()
        customer = use_case.create(
            name=serializer.validated_data['name'],
            phone_number=serializer.validated_data['phone_number'],
            email=serializer.validated_data['email'],
            vat_id=serializer.validated_data['vat_id'],
        )
        result = CustomerSerializer(customer)
        return Response(result.data)