from uuid import uuid4
from typing import List
from datetime import date

from domain.model import ElectricAgreement

from domain.repositories.agreement_repository import ElectricAgreementRepository
from infraestructure.django.persistance.django_models import ElectricAgreementDjangoModel, ElectricAgreementHolderDjangoModel
from project.src.apps.customers.infraestructure.django.persistence.django_models import CustomerDjangoModel
from project.src.apps.customers.infraestructure.django.repositories.django_customer_repository import CustomerDjangoRepository


class ElectricAgreementDjangoRepository(ElectricAgreementRepository):
    
    def get_by_id(self, id: uuid4) -> ElectricAgreement:
        return ElectricAgreementDjangoModel.objects.get(id=id).to_domain()

    def get_by_date_gte(self, start_date: date) -> List(ElectricAgreement):
        items = ElectricAgreementDjangoModel.objects.filter(start_date__gte=start_date)
        result = [i.to_domain() for i in items]
        return result

    def save(self, agreement: ElectricAgreement):
        
        holder = CustomerDjangoRepository.get_by_id(agreement.holder.id)
        payer = 
        try:
            object = ElectricAgreementDjangoModel.objects.get(id=agreement.id)
        except ElectricAgreementDjangoModel.DoesNotExist:
            object = ElectricAgreement(id=agreement.id)
        holder = agreement.holder.

        for holder in agreement.list_holders():
            if not ElectricAgreementHolderDjangoModel.objects.get(agreement_id=agreement.id, holder_id=holder.id).exists():
                ElectricAgreementHolderDjangoModel.objects.create(agreement=object, holder=holder)
    
    def get_holders(self, id: uuid4):
        items = ElectricAgreementHolderDjangoModel.objects.filter(agreement_pk=id)
        result = [i.to_domain() for i in items]
        return result
