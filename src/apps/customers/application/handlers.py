from apps.customers.domain import events

from apps.customers.domain.repositories.customer_repository import CustomerRepository


def send_email_info(event: events.NewCustomerCreated):
    print(f'send email for: {event.name}')


def create_new_customer(event: events.NewCustomerToBeCreated, repository: CustomerRepository):
    _customer = event.to_domain_model_dict()
    repository.save(**_customer)