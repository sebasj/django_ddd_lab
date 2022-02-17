from __future__ import annotations
from dataclasses import dataclass
from datetime import date
from typing import Optional, List, Set

import datetime


class CustomerExistsException(Exception):
    pass


class Address:
    def __init__(
        self,
        street: str,
        number: str,
        cp: str,
        poblation: str,
        desc: str
    ):
        self.street = street
        self.number = number
        self.cp = cp
        self.poblation = poblation
        self.desc = desc

    def __repr__(self) -> str:
        return f'{self.desc}; {self.poblation}; {self.street}; {self.cp} '

    def add_obs(self, obs: str):
        self.obs += obs


class Customer:
    def __init__(
        self,
        name: str,
        phone_number: str,
        email: str,
        vat_id: str,
    ): 
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.vat_id = vat_id
        self.contracts = []
        self.deleted = False
        self.active = False    
        self.created_at = datetime.datetime.now()

    def __repr__(self) -> str:
        return f'{self.name}; {self.vat_id}; {self.phone_number}; {self.email} '

    def __eq__(self, other: object) -> bool:
        if not isinstance(Customer):
            return False
        return self.vat_id == other.vat_id
    
    def add_obs(self, obs: str):
        self.obs += obs

    def set_active(self):
        self.active = True
    
    def set_deleted(self):
        self.deleted = True
    
    def add_obs(self, obs: str):
        _aux = []
        _aux.append('New comments: ')
        _aux.append(datetime.datetime.now())
        _aux.append(obs)
        self.obs += ''.join(obs)

    def add_address(
        self, 
        street: str,
        number: str,
        cp: str,
        poblation: str,
        desc: str
    ):
        self.add_address = Address(street=street, number=number, cp=cp, poblation=poblation, desc=desc)