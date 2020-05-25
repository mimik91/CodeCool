from model.sales import sales
from view import terminal as view
from model import util

def list_transactions():
    topic="SALES table"
    view.print_message(topic)
    table=sales.read_record()
    table.insert(0, sales.HEADERS)
    view.print_table(table)


def add_transaction():
    HEADERS = ["Customer", "Product", "Price", "Date"]
    id_number = util.generate_id()
    labels = view.get_inputs(HEADERS)
    table = sales.create_item(id_number, labels[0], labels[1], labels[2], labels[3])
    table.insert(0, sales.HEADERS)
    view.print_table(table)


def update_transaction():
    HEADERS = ["record_id", "Customer", "Product", "Price", "Date"]
    labels=view.get_inputs(HEADERS)
    table=sales.modify_item(labels[0], labels[1], labels[2], labels[3], labels[4])
    table.insert(0, sales.HEADERS)
    view.print_table(table)
    

def delete_transaction():
    label=view.get_input("record_id")
    table=sales.remove_record(label)
    table.insert(0, sales.HEADERS)
    view.print_table(table)


def get_biggest_revenue_transaction():
    view.print_general_results((sales.max_revenue()),"Bigest revenue")


def get_biggest_revenue_product():
    view.print_general_results((sales.best_total_revenue()),"Best selling item by amount")


def count_transactions_between():
    labels=["data1","data2"]
    dates=view.get_inputs(labels)
    view.print_general_results((sales.count_transactions(dates[0],dates[1])),"Amount of transaction in this period")


def sum_transactions_between():
    labels=["data1","data2"]
    dates=view.get_inputs(labels)
    view.print_general_results((sales.revenue_in_dates(dates[0],dates[1])),"Amount of transaction in this period")


def run_operation(option):
    if option == 1:
        list_transactions()
    elif option == 2:
        add_transaction()
    elif option == 3:
        update_transaction()
    elif option == 4:
        delete_transaction()
    elif option == 5:
        get_biggest_revenue_transaction()
    elif option == 6:
        get_biggest_revenue_product()
    elif option == 7:
        count_transactions_between()
    elif option == 8:
        sum_transactions_between()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List transactions",
               "Add new transaction",
               "Update transaction",
               "Remove transaction",
               "Get the transaction that made the biggest revenue",
               "Get the product that made the biggest revenue altogether",
               "Count number of transactions between",
               "Sum number of transactions between"]
    view.print_menu("Sales", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
