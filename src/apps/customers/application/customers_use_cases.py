import uuid
from typing import List

from apps.customers.domain.models import Customer
from apps.customers.domain.repositories.customer_repository import CustomerRepository


class CustomerUseCaseMixin:
    def __init__(self, customers_repository: CustomerRepository):
        self.customers_repository = customers_repository


class CustomersListUseCase(CustomerUseCaseMixin):
    def execute(self) -> List[Customer]:
        customers = self.customers_repository.list()
        return customers


class RetrieveCustomerUseCase(CustomerUseCaseMixin):

    def execute(self, customer_id: uuid.uuid4) -> Customer:
        customer = self.customers_repository.get_by_id(id=customer_id)
        return customer


class CustomerCreateUseCase(CustomerUseCaseMixin):    
    def create(self, name, phone_number, email, vat_id) -> Customer:
        customer = Customer(
            name=name, phone_number=phone_number, email=email, vat_id=vat_id
        )
        return self.customers_repository.save(customer=customer)