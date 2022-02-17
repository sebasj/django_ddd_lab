import uuid

from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime, date
from typing import Optional, List, Set

from customers.domain import Customer, Address


class ElectricAgreementException(Exception):
    pass


class ElectricAgreement:
    def __init__(
        self,
        holder: Customer,
        payer: Customer,
        service_address: Address,
        billing_address: Address,
        start_date: date,
        id: uuid.uuid4 = uuid.uuid4(),
        holders: List[Customer] = Set(),
        created_at: datetime = datetime.now()
    ):
        self.holder = holder
        self.payer = payer
        self.service_address = service_address
        self.billing_address = billing_address
        self.start_date = start_date
        self.end_date = None
        self.id = id
        self.holders = holders
        self.created_at = created_at 

    def add_holder(self, new_holder: Customer):
        self.holders.add(new_holder)
    
    def finish_agreement(self, end_date: date):
        self.end_date = end_date

    def list_holders(self) -> List(Customer):
        result = []
        result.append(self.holder)
        result.append(self.holders)
        return result
