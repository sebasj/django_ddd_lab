import abc
import uuid
from typing import List

from apps.customers.domain.models import Customer


class CustomerRepository(abc.ABC):
    @abc.abstractmethod
    def get_by_id(self, id: uuid.uuid4) -> Customer:
        raise NotImplementedError

    
    @abc.abstractmethod
    def save(self, customer: Customer) -> Customer:
        raise NotImplementedError
    

    @abc.abstractmethod
    def list(self) -> List[Customer]:
        raise NotImplementedError