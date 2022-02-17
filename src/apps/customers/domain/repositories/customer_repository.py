import abc
import uuid
from typing import List

from domain.model import Customer


class CustomerRepository(abc.ABC):
    @abs.abstractmethod
    def get_by_id(self, id: uuid.uuid4) -> Customer:
        raise NotImplementedError

    
    @abs.abstractmethod
    def save(self, customer: Customer):
        raise NotImplementedError
    
    @abs.abstractmethod
    def list(self) -> List(Customer):
        raise NotImplementedError