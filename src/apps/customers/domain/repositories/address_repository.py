import abc

from typing import List

from apps.customers.domain.models import Address


class AddressRepository(abc.ABC):
    @abc.abstractmethod
    def filter_by_street(self, street: str) -> List[Address]:
        raise NotImplementedError

    @abc.abstractmethod
    def filter_by_cp(self, cp: str) -> List[Address]:
        raise NotImplementedError
    
    @abc.abstractmethod
    def filter_by_customer(self, id: int) -> Address:
        raise NotImplementedError

    @abc.abstractmethod
    def save(self, address: Address):
        raise NotImplementedError
    