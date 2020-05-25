from model.hr import hr
from model import util
from view import terminal as view


def list_employees():
    message = "HR table"
    view.print_message(message)
    table = hr.read_data()
    table.insert(0, hr.HEADERS)
    view.print_table(table)


def add_employee():
    HEADERS = ["Name", "Date of birth", "Department", "Clearance"]
    id_number = util.generate_id()
    labels = view.get_inputs(HEADERS)
    table = hr.create_data(id_number, labels[0], labels[1], labels[2], labels[3])
    table.insert(0, hr.HEADERS)
    view.print_table(table)


def update_employee():
    HEADERS = ["Id", "Name", "Date of birth", "Department", "Clearance"]
    labels = view.get_inputs(HEADERS)
    table = hr.update_data(labels[0], labels[1], labels[2], labels[3], labels[4])
    table.insert(0, hr.HEADERS)
    view.print_table(table)


def delete_employee():
    id_number = view.get_input("Please enter employee's id number")
    table = hr.delete_data(id_number)
    table.insert(0, hr.HEADERS)
    view.print_table(table)


def get_oldest_and_youngest():
    result = hr.names_tuple()
    view.print_general_results(result, "The youngest and the oldest employees are")


def get_average_age():
    result = hr.average_age()
    view.print_general_results(result, "The average age of our employees is")


def next_birthdays():
    input_date = view.get_input("Please enter a date in format year-month-day")
    result = hr.Bday_in_2_weeks(input_date)
    view.print_general_results(result, "Birthday(s) in the upcomin 14 days have")


def count_employees_with_clearance():
    label = "Please enter employee's clearance level from 0 (lowest) to 7 (highest)"
    given_level = view.get_input(label)
    result = hr.given_clearance_level(given_level)
    view.print_general_results(result, "Number of employees with at least given clearance level is")


def count_employees_per_department():
    result = hr.employees_per_department()
    view.print_general_results(result, "Here are the numbers of employees per departament")


def run_operation(option):
    if option == 1:
        list_employees()
    elif option == 2:
        add_employee()
    elif option == 3:
        update_employee()
    elif option == 4:
        delete_employee()
    elif option == 5:
        get_oldest_and_youngest()
    elif option == 6:
        get_average_age()
    elif option == 7:
        next_birthdays()
    elif option == 8:
        count_employees_with_clearance()
    elif option == 9:
        count_employees_per_department()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List employees",
               "Add new employee",
               "Update employee",
               "Remove employee",
               "Oldest and youngest employees",
               "Employees average age",
               "Employees with birthdays in the next two weeks",
               "Employees with clearance level",
               "Employee numbers by department"]
    view.print_menu("Human resources", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
