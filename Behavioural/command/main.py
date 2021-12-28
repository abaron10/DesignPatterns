from CustomerService import CustomerService
from AddCustomerCommand import AddCustomerCommand
from Button import Button
if __name__ == '__main__':
    service = CustomerService()
    command = AddCustomerCommand(service)
    button  =  Button(command)

    button.click()