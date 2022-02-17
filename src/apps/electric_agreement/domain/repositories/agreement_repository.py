import abc

from datetime import date
from typing import List
from uuid import uuid4

from domain.model import ElectricAgreement


class ElectricAgreementRepository(abc.ABC):
    @abs.abstractmethod
    def get_by_id(self, id: uuid4) -> ElectricAgreement:
        raise NotImplementedError

    @abs.abstractmethod
    def get_by_date_gte(self, start_date: date) -> List(ElectricAgreement):
        raise NotImplementedError

    @abs.abstractmethod
    def save(self, agreement: ElectricAgreement):
        raise NotImplementedError
    
    @abs.abstractmethod
    def get_holders(self, id: uuid4):
        raise NotImplementedError