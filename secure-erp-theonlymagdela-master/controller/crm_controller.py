""" Customer Relationship Management (CRM) CONTROLER module """

from model.crm import crm
from model.crm.crm import HEADERS, HEADER_ID, HEADER_NAME, HEADER_EMAIL, HEADER_SUBSCRIBE
from view import terminal as view


# ------------------------------------ main module functions --------------------------------------

def list_customers():
    '''Returns the dataset with the header in the first row.'''
    table = crm.read_data()
    table.insert(0, HEADERS)
    view.print_table(table)


def add_customer():
    '''Creates the new customer in the dataset.'''
    PREFIX = "New Customer"

    # prepares labels to ask User about the new customer data
    labels = (f"{PREFIX} {HEADERS[HEADER_NAME]}",
              f"{PREFIX} {HEADERS[HEADER_EMAIL]}",
              f"{PREFIX} {HEADERS[HEADER_SUBSCRIBE]}")

    customer_data = view.get_inputs(labels)
    crm.create_item(customer_data)

    view.print_general_results(customer_data, "New Customer added")


def update_customer():
    '''Updates informations of the customer in the dataset.'''
    PREFIX = "Update"
    SUFIX = "(empty -> no change)"

    # prepares labels to ask User about the new customer data
    labels = (f"Enter Customer {HEADERS[HEADER_ID]} to make changes",
              f"{PREFIX} {HEADERS[HEADER_NAME]} {SUFIX}",
              f"{PREFIX} {HEADERS[HEADER_EMAIL]}{SUFIX}",
              f"{PREFIX} {HEADERS[HEADER_SUBSCRIBE]}{SUFIX}")

    data_to_update = view.get_inputs(labels)
    crm.update_item(data_to_update)

    view.print_message(f"Customer '{data_to_update[HEADER_ID]}' updated")


def delete_customer():
    '''Deletes the customer from the dataset.'''
    crm.delete_item(view.get_input("Get Customers ID to delete Customer"))
    view.print_message("Customer deleted")


def get_subscribed_emails():
    '''Lists all subscribed e-mails.'''
    view.print_general_results(crm.get_subscribed_emails(), "Subscribed emails")


# ---------------------------------------- menu functions -----------------------------------------

def run_operation(option):
    if option == 1:
        list_customers()
    elif option == 2:
        add_customer()
    elif option == 3:
        update_customer()
    elif option == 4:
        delete_customer()
    elif option == 5:
        get_subscribed_emails()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List customers",
               "Add new customer",
               "Update customer",
               "Remove customer",
               "Subscribed customer emails"]
    view.print_menu("Customer Relationship Management", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
