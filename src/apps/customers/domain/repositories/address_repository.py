import abc

from typing import List

from domain.model import Address


class AddressRepository(abc.ABC):
    @abs.abstractmethod
    def filter_by_street(self, street: str) -> List[Address]:
        raise NotImplementedError

    @abs.abstractmethod
    def filter_by_cp(self, cp: str) -> List[Address]:
        raise NotImplementedError
    
    @abs.abstractmethod
    def save(self, address: Address):
        raise NotImplementedError
    