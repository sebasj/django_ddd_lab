import abc

from customers.domain.repositories import customer_repository, address_repository



class CustomersAbstractUnitOfWork(abc.ABC):
    customers_repository: customer_repository.CustomerRepository

    def __exit__(self, *args):
        self.rollback()


    @abs.abstractmethod
    def commit(self):
        raise NotImplementedError

    @abs.abstractmethod
    def rollback(self):
        raise NotImplementedError


class AddressAbstractUnitOfWork(abc.ABC):
    address_repository: address_repository.AddressRepository

    def __exit__(self, *args):
        self.rollback()


    @abs.abstractmethod
    def commit(self):
        raise NotImplementedError

    @abs.abstractmethod
    def rollback(self):
        raise NotImplementedError
