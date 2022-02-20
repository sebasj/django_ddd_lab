import uuid
from typing import List

from customers.domain.models import Customer, Address

from customers.domain.repositories.customer_repository import CustomerRepository
from customers.domain.repositories.address_repository import AddressRepository

from customers.infraestructure.django.models import CustomerDjangoModel, AddressDjangoModel


class CustomerDjangoRepository(CustomerRepository):
    
    def __init__(self):
        super().__init__() # Initializes CustomerRepository.seen attribute

    def _get_by_id(self, id: uuid.uuid4) -> Customer:
        return CustomerDjangoModel.objects.get(id=id).to_domain()

    def _save(self, customer: Customer) -> Customer:
        try:
            object = CustomerDjangoModel.objects.get(vat_id=customer.vat_id)
        except CustomerDjangoModel.DoesNotExist:
            object = CustomerDjangoModel(vat_id=customer.vat_id)
        object.name = customer.name
        object.phone_number = customer.phone_number
        object.email = customer.email
        object.obs = customer.obs
        object.save()
        return object

    def list(self) -> List[Customer]:
        return [b.to_domain() for b in CustomerDjangoModel.objects.all()]


class AddressDjangoRepository(AddressRepository):
    
    def filter_by_street(self, street: str) -> List[Address]:
        temp_results = AddressDjangoModel.objects.filter(street__icontains=street)
        results = []
        for r in temp_results:
            results.append(r.to_domain())
        return results

    def filter_by_cp(self, cp: str) -> List[Address]:
        temp_results = AddressDjangoModel.objects.filter(cp=cp)
        results = []
        for r in temp_results:
            results.append(r.to_domain())
        return results

    def filter_by_customer(self, id: int) -> Address:
        return AddressDjangoModel.object.get(customer_pk=id)

    def save(self, address: Address):
        try:
            object = AddressDjangoModel.objects.get(id=object.id)
        except AddressDjangoModel.DoesNotExist:
            object = AddressDjangoModel(id=address.id)
        object.customer = address.customer
        object.street = address.street
        object.number = address.number
        object.cp = address.cp
        object.poblation = address.poblation
        object.desc = address.obs
        object.save()
