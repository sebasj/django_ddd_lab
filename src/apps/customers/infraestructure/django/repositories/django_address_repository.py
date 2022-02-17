import abc

from typing import List

from domain.model import Address

from customers.domain.repositories.address_repository import AddressRepository
from customers.infraestructure.persistence.django.django_models import AddressDjangoModel


class AddressDjangoRepository(AddressRepository):
    
    def filter_by_street(self, street: str) -> List[Address]:
        temp_results = AddressDjangoModel.objects.filter(street__icontains=street)
        results = []
        for r in temp_results:
            results.append(r.to_domain())
        return results

    def filter_by_cp(self, cp: str) -> List[Address]:
        temp_results = AddressDjangoModel.objects.filter(cp=cp)
        results = []
        for r in temp_results:
            results.append(r.to_domain())
        return results

    def save(self, address: Address):
        try:
            object = AddressDjangoModel.objects.get(id=object.id)
        except AddressDjangoModel.DoesNotExist:
            object = AddressDjangoModel(id=address.id)
        object.street = address.street
        object.number = address.number
        object.cp = address.cp
        object.poblation = address.poblation
        object.desc = address.obs
        object.save()
