import abc
import uuid
from typing import List

from apps.customers.domain.models import Customer


class CustomerRepository(abc.ABC):
    def __init__(self):
        self.customers_seen = set()
    
    def collect_new_events(self):
        for customer in self.seen:
            while customer.events:
                yield customer.events.pop(0)

    def add(self, customer: Customer):
        self.customers_seen.add(customer)

    def get_by_id(self, id: uuid.uuid4) -> Customer:
        customer = self._get_by_id(id)
        self.add(customer)
        return customer

    def save(self, customer: Customer) -> Customer:
        customer = self._save(customer)
        self.add(customer)
        return customer

    @abc.abstractmethod
    def _get_by_id(self, id: uuid.uuid4) -> Customer:
        raise NotImplementedError
        
    @abc.abstractmethod
    def _save(self, customer: Customer) -> Customer:
        raise NotImplementedError

    @abc.abstractmethod
    def list(self) -> List[Customer]:
        raise NotImplementedError