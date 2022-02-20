import abc
import uuid
from typing import List

from apps.customers.domain.models import Customer

from apps.customers.domain.repositories.customer_repository import CustomerRepository


class CustomerFastAPIRepository(CustomerRepository):
    
    def get_by_id(self, id: uuid.uuid4) -> Customer:
        return Customer(
            name='test',
            vat_id='test',
            phone_number='test',
            email='lucas@lucas.com',
            obs='lucas est',
        )

    def save(self, customer: Customer) -> Customer:
        return customer
    
    def list(self) -> List[Customer]:
        return [
            Customer(
                name='test',
                vat_id='test',
                phone_number='test',
                email='lucas@lucas.com',
                obs='lucas est',
            ),
            Customer(
                name='test1',
                vat_id='test1',
                phone_number='test1',
                email='lucas@lucas.com',
                obs='lucas est',
            )
        ]