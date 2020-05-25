""" Human resources (HR) module
Data table structure:
    - id (string)
    - name (string)
    - birth date (string): in ISO 8601 format (like 1989-03-21)
    - department (string)
    - clearance level (int): from 0 (lowest) to 7 (highest)
"""

from model import data_manager, util
from datetime import date, timedelta

DATAFILE = "model/hr/hr.csv"
HEADERS = ["Id", "Name", "Date of birth", "Department", "Clearance"]

ID = 0
NAME = 1
BIRTH_DATE = 2
DEPARTAMENT = 3
CLEARANCE_LEVEL = 4


def create_data(id_number, em_name, bday_date, dept, clearance_level):
    '''
    adding a new employee
    '''
    employees_list = data_manager.read_table_from_file(DATAFILE)
    emp_list = []

    for element in employees_list:
        emp_list.append(element)
    new_employee = [id_number, em_name, bday_date, dept, clearance_level]
    emp_list.append(new_employee)

    data_manager.write_table_to_file(DATAFILE, emp_list)

    return emp_list


def read_data():
    '''
    matrix to display data accurately in view module
    '''
    employees_list = data_manager.read_table_from_file(DATAFILE)
    the_list = []

    for employee_data in employees_list:
        the_list.append(employee_data)

    return the_list


def update_data(id_number, em_name, bday_date, dept, clearance_level):
    '''
    making changes in already existing data, 5 possible changes
    '''
    employees_list = data_manager.read_table_from_file(DATAFILE)
    updated_list = []

    for employee in employees_list:
        if id_number in employee:
            employee = [id_number, em_name, bday_date, dept, clearance_level]
            updated_list.append(employee)
        else:
            updated_list.append(employee)
    employees_list = updated_list

    data_manager.write_table_to_file(DATAFILE, employees_list)

    return employees_list


def delete_data(id_number):
    '''
    deleting employee based on id
    '''
    cos = []
    employees_list = data_manager.read_table_from_file(DATAFILE)

    for employee_lst in employees_list:
        if id_number in employee_lst:
            pass
        else:
            cos.append(employee_lst)
    employees_list = cos

    data_manager.write_table_to_file(DATAFILE, employees_list)

    return employees_list


def names_tuple():
    '''
    Returns the names of the oldest and the youngest employees as a tuple
    '''
    employees_list = data_manager.read_table_from_file(DATAFILE)
    difference_list = []

    for i in range(len(employees_list)):
        bday_date = date.fromisoformat(employees_list[i][BIRTH_DATE]), employees_list[i][NAME]
        difference = bday_date[0] - date.today(), bday_date[1]
        difference_list.append(difference)
        min_age = max(difference_list)
        max_age = min(difference_list)

    youngest_oldest = (min_age[1], max_age[1])

    return youngest_oldest


def average_age():
    date_list = []
    employees_list = data_manager.read_table_from_file(DATAFILE)
    for the_date in employees_list:
        date_list.append(the_date[BIRTH_DATE])

    TEMP = []
    TEMP_2 = []
    for i in range(len(date_list)):
        employee_bday = date_list[i].replace("-", ",")
        employee_bday = employee_bday.split(",")
        for element in employee_bday:
            element = int(element)
            TEMP_2.append(element)
        employee_bday = TEMP_2
        TEMP_2 = []
        TEMP.append(employee_bday)
    employees_bdays = TEMP

    ages = []
    for i in employees_bdays:
        days_in_year = 365.2425
        age_count = int((date.today() - date(i[0], i[1], i[2])).days / days_in_year)
        ages.append(age_count)

    age = 0
    total = 0
    for age in ages:
        total += age
    average = round(total / len(ages))

    return average


def Bday_in_2_weeks(input_date):
    '''
    Returns the names of employees having birthdays within the two weeks starting from the given date
    '''
    employees_list = data_manager.read_table_from_file(DATAFILE)
    given_date = date.fromisoformat(input_date)
    given_year = int(input_date[:4])
    list_of_employers = []

    bdays_range = given_date + timedelta(days=14)

    for j in range(2):
        given_year += j
        for i in range(len(employees_list)):
            data = date.fromisoformat(employees_list[i][BIRTH_DATE])
            data = data.replace(year=given_year)
            DIFFERENCE = timedelta(days=14) - (bdays_range - data)

            if DIFFERENCE <= timedelta(days=14) and DIFFERENCE >= timedelta(days=0):
                list_of_employers.append(employees_list[i][NAME])

    return list_of_employers


def given_clearance_level(given_level):
    '''
    Returns the number of employees with at least the given clearance level
    '''
    employees_list = data_manager.read_table_from_file(DATAFILE)
    count_employees = 0
    for i in range(len(employees_list)):
        if int(employees_list[i][CLEARANCE_LEVEL]) >= int(given_level):
            count_employees += 1

    return count_employees


def employees_per_department():
    '''
    Returns the number of employees per department in a dictionary (like {'dep1': 5, 'dep2': 11})
    '''
    employees_list = data_manager.read_table_from_file(DATAFILE)
    new_list = []

    for i in employees_list:
        new_list.append(i[DEPARTAMENT])
    result = dict((i, new_list.count(i)) for i in new_list)

    return result
