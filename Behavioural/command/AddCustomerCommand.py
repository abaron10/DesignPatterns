
from Command import Command
class AddCustomerCommand(Command):

    def __init__(self, customerService):
        self.service = customerService

    def execute(self):
        self.service.addCustomer()
