import uuid
from typing import List

from customers.domain.model import Customer
from customers.domain.model import Address

from customers.domain.repositories.customer_repository import CustomerRepository
from customers.domain.repositories.address_repository import AddressRepository

from customers.infraestructure.persistence.django.django_models import CustomerDjangoModel


class CustomerDjangoRepository(CustomerRepository):
    
    def get_by_id(self, id: uuid.uuid4) -> Customer:
        return CustomerDjangoModel.objects.get(id=id).to_domain()

    def save(customer: Customer):
        try:
            object = CustomerDjangoModel.objects.get(vat_id=object.vat_id)
        except CustomerDjangoModel.DoesNotExist:
            object = CustomerDjangoModel(vat_id=customer.vat_id)
        object.name = customer.name
        object.phone_number = customer.phone_number
        object.email = customer.email
        object.desc = customer.desc
        object.desc = customer.obs
        object.save()

    def list(self) -> List(Customer):
        return [b.to_domain() for b in CustomerDjangoModel.objects.all()]



