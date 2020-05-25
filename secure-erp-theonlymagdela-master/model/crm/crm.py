""" Customer Relationship Management (CRM) module

Data table structure:
    - id (string)
    - name (string)
    - email (string)
    - subscribed (int): Is subscribed to the newsletter? 1: yes, 0: no
"""


# ----------------------------- import modules & constant definitions -----------------------------

from model import data_manager, util


# files
DATAFILE = "model/crm/crm.csv"
# headers identifiers and names
HEADERS = ["id", "name", "email", "subscribed"]
HEADER_ID = 0
HEADER_NAME = 1
HEADER_EMAIL = 2
HEADER_SUBSCRIBE = 3
# subscribed to the newsletter
SUBSCRIBED_NO = 0
SUBSCRIBED_YES = 1


# ------------------------------------ main module functions --------------------------------------

def create_item(new_item, file_name=DATAFILE):
    '''Creates new sent data in a dataset.'''
    new_item.insert(HEADER_ID, get_new_id())

    table = read_data(file_name)
    table.append(new_item)
    write_data(table, file_name)


def read_item(item_id, file_name=DATAFILE):
    '''Reads sent data in a dataset.'''
    table = read_data(file_name)
    item_index = get_item_index(table, item_id)

    return table[item_index]


def update_item(item_to_update, file_name=DATAFILE):
    '''Updates sent data in a dataset.'''
    table = read_data(file_name)
    item_index = get_item_index(table, item_to_update[HEADER_ID])

    # checks all updated data, if "" occurs, it leaves the data unchanged
    for data_index in range(1, len(table[item_index])):  # from 1 - ID's cannot be modified
        if item_to_update[data_index] != "":
            table[item_index][data_index] = item_to_update[data_index]

    write_data(table, file_name)


def delete_item(item_id, file_name=DATAFILE):
    '''Deletes sent data in a dataset.'''
    table = read_data(file_name)
    item_index = get_item_index(table, item_id)
    table.pop(item_index)
    write_data(table, file_name)


def get_subscribed_emails(file_name=DATAFILE):
    '''Returns e-mails from a dataset'''
    subscribed = collect_data(HEADER_SUBSCRIBE, file_name)
    emails = collect_data(HEADER_EMAIL, file_name)

    subscribed_email = []
    for index in range(len(emails)):
        if int(subscribed[index]) == SUBSCRIBED_YES:
            subscribed_email.append(emails[index])

    return subscribed_email


# -------------------------------------- internal functions ---------------------------------------

def collect_data(column_number, file_name=DATAFILE):
    '''Returns collected data by column identifier'''
    table = read_data(file_name)

    collected_data = []
    for item in table:
        collected_data.append(item[column_number])

    return collected_data


def get_item_index(table, item_id):
    '''Trys find by id and returns item index in a dataset.'''
    for item in table:
        if item[HEADER_ID] == item_id:
            return table.index(item)
    else:
        raise ValueError("Item not found in the dataset")


def get_new_id(file_name=DATAFILE):
    '''Creats new unique ID for the new user.'''
    new_id = util.generate_id()

    # checks new ID in existing IDs in the dataset
    current_ids = collect_data(HEADER_ID, file_name)
    while new_id in current_ids:
        new_id = util.generate_id()

    return new_id


# ------------------------------------ read & write functions -------------------------------------

def read_data(file_name=DATAFILE):
    '''Reads all data from file. As an option, it adds a header to the data.'''
    table = data_manager.read_table_from_file(file_name)
    if table == []:  # error: reading data from file faild
        raise IOError("Error reading data from file")

    return table


def write_data(table, file_name=DATAFILE):
    '''Writes all data to file.'''
    data_manager.write_table_to_file(file_name, table)
