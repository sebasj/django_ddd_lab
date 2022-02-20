from dataclasses import dataclass


class Event:
    pass


@dataclass
class NewCustomerToBeCreated(Event):
    name: str
    phone_number: str
    email: str
    vat_id: str
    obs: str

    def to_domain_model_dict(self):
        return {
            'name': self.name,
            'phone_number': self.phone_number,
            'email': self.email,
            'vat_id': self.vat_id,
            'obs': self.obs
        }


@dataclass
class NewCustomerCreated(Event):
    name: str
    phone_number: str
    email: str