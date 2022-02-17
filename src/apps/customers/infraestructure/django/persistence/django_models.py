
from django.db import models

from customers.domain.model import Customer as domain_customer
from customers.domain.model import Address as domain_address



class CustomerDjangoModel( models.Model):
    vat_id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=75)
    phone_number = models.CharField(max_length=12)
    email = models.EmailField(max_length=50, null=True, blank=True)
    desc = models.CharField(max_length=200)
    obs = models.TextField(null=True, blank=True)

    
    def to_domain(self) -> domain_customer:
        return domain_customer(
            vat_id=self.vat_id,
            name=self.name,
            phone_number=self.phone_number,
            email=self.email,
            desc=self.email,
            obs=self.obs
        )
        

class AddressDjangoModel(models.Model):
    street = models.CharField(max_length=255)
    number = models.CharField(max_length=5)
    cp = models.CharField(max_length=10)
    poblation = models.CharField(max_length=50)
    desc = models.CharField(max_length=200)
    obs = models.TextField(null=True, blank=True)
    customer = models.ForeignKey(CustomerDjangoModel)

    def to_domain(self) -> domain_address:
        return domain_address(
            id=self.id,
            street=self.street,
            number=self.number,
            cp=self.cp,
            poblation=self.poblation,
            desc=self.desc
        )