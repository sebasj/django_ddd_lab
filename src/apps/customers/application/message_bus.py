from typing import Union, List

from apps.customers.domain import events, commands
from apps.customers.domain.repositories.customer_repository import CustomerRepository

from . import handlers

import logging
logger = logging.getLogger(__name__)


Message = Union[commands.Command, events.Event]


def handle(message: Message, repository: CustomerRepository):
    results = []
    queue = [message]
    while queue:
        message = queue.pop(0)
        if isinstance(message, events.Event):
            handle_event(message, queue, repository)
        elif isinstance(message, commands.Command):
            command_result = handle_command(message, queue, repository)
            results.append(command_result)
        for handler in HANDLERS[type(event)]:
            handler(message, repository)
        else:
            raise Exception('Error Processing Messages')


def handle_event(
    event: events.Event,
    queue: List[Message],
    repository: CustomerRepository
):
    for handler in EVENT_HANDLERS[type(event)]:
        try:
            logger.debug('handling event {} with handler {}'.format(event, handler))
            handler(event, repository)
            queue.extend(repository.collect_new_events())
        except Exception:
            logger.exception('EXCEPTION AT: handling event {} with handler {}'.format(event, handler))
            continue

EVENT_HANDLERS = {
    events.NewCustomerCreated: [handlers.send_email_info,],
    events.NewCustomerCreated: [handlers.create_new_customer,],
}


def handle_command(
    command: commands.Command,
    queue: List[Message],
    repository: CustomerRepository
):
    for handler in EVENT_HANDLERS[type(event)]:
        try:
            logger.debug('handling commands {} with handler {}'.format(event, handler))
            handler = COMMAND_HANDLERS[type(command)]
            result = handler(command, repository)
            queue.extend(repository.collect_new_events())
            return result
        except Exception:
            logger.exception('EXCEPTION AT: handling command {} with handler {}'.format(event, handler))
            raise

COMMAND_HANDLERS = {}
