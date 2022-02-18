import uuid
from typing import Optional, List, Set

from customers.domain.model import Customer
from customers.domain.repositories.customer_repository import CustomerRepository


class CustomerUseCaseMixin:
    def __init__(self, customers_repository: CustomerRepository):
        self.customers_repository = customer_repository


class CustomersListUseCase(CustomerUseCaseMixin):
    def execute(self) -> List(Customer):
        customers = self.customers_repository.list()
        return customers


class RetrieveCustomerUseCase(CustomerUseCaseMixin):

    def execute(self, customer_id: uuid.uuid4) -> Customer:
        customer = self.customers_repository.get_by_id(id=customer_id)
        return customer

    