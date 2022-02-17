from tracemalloc import start
import uuid

from django.db import models

from electric_agreement.domain.model import ElectricAgreement as domain_agreement
from customers.infraestructure.django.persistence.django_models import CustomerDjangoModel, AddressDjangoModel


class ElectricAgreementDjangoModel(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    holder = models.ForeignKey(CustomerDjangoModel)
    payer = models.ForeignKey(CustomerDjangoModel, blank=True, null=True)
    service_address = models.ForeignKey(AddressDjangoModel, blank=True, null=True)
    billing_address = models.ForeignKey(AddressDjangoModel, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    holders = models.ForeignKey(ElectricAgreementHolderDjangoModel, blank=True, null=True, )
    created_at = models.DateTimeField(auto_now_add=True)

    def to_domain(self) -> domain_agreement:
        holders = [h.to_domain() for h in self.holders_set.all()]
        agreement = domain_agreement(
            id=self.id,
            holder=self.holder.to_domain(),
            payer=self.payer.to_domain(),
            service_address=self.service_address.to_domain(),
            billing_address=self.billing_address.to_domain(),
            start_date=self.start_date,
            end_date=self.end_date,
            holders=holders,
        ) 
        return agreement


class ElectricAgreementHolderDjangoModel(models.Model):
    agreement = models.ForeignKey(ElectricAgreementDjangoModel)
    holder = models.ForeignKey(CustomerDjangoModel)