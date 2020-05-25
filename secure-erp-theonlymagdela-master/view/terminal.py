

def print_menu(title, list_options):
    """Prints options in standard menu format like this:

    Main menu:
    (1) Store manager
    (2) Human resources manager
    (3) Inventory manager
    (0) Exit program

    Args:
        title (str): the title of the menu (first row)
        list_options (list): list of the menu options (listed starting from 1, 0th element goes to the end)
    """
    print(title)
    print()
    for index, option in enumerate(list_options):
        print(f"({index}) {option}")


def print_message(message):
    """Prints a single message to the terminal.

    Args:
        message: str - the message
    """
    print(f"\n{message}")


def print_general_results(result, label):
    if type(result) is list:
        print(label + ": ", "\n", ("; ").join(result))
    elif type(result) is float or type(result) is int:
        print(label + ": ", round(result, 2))
    elif type(result) is tuple:
        print(label+":\n", result)
    elif type(result) is dict:
        list_to_print = []
        for key, value in result.items():
            list_to_print = list_to_print + [str(key) + ": " + str(value)]
        print_general_results(list_to_print, label)
    else:
        raise ValueError


def print_table(table):
    """Prints tabular data like below.

    Args:
        table: list of lists - the table to print out

            /--------------------------------\\
            |   id   |   product  |   type   |
            |--------|------------|----------|
            |   0    |  Bazooka   | portable |
            |--------|------------|----------|
            |   1    | Sidewinder | missile  |
            \\--------------------------------/
    """
    COL_MARGIN_SIZE = 1
    COL_SEPARATOR = "|"
    ROW_SEPARATOR = "-"
    TABLE_CORNER_A = "/"
    TABLE_CORNER_B = "\\"

    def get_column_widths(table):
        '''Returns the list of the width of all columns in the table.'''

        def prepare_list(table):
            '''Prepares a list with 0 values in the number corresponding to the number of columns in the table.'''
            prepared_list = []
            for _ in range(len(table[0])):  # table[0] - first row
                prepared_list.append(0)
            return prepared_list

        # prepare_column_widths_list main code
        column_widths = prepare_list(table)
        for row in table:
            for column in row:
                column_width = COL_MARGIN_SIZE + len(column) + COL_MARGIN_SIZE  # margin + string + margin
                current_index = row.index(column)
                if column_width > column_widths[current_index]:  # remembers a wider column
                    column_widths[current_index] = column_width

        return column_widths

    def get_table_width(column_widths):
        '''Returns the width of the table.'''
        table_width = 1  # 1 - first vertical separator
        for index in range(len(column_widths)):
            table_width += column_widths[index] + 1  # +1 - last vertical separator

        return table_width

    def display_row_separator(table_width, sep_type="middle"):
        '''
        Prints row separator.
            type: "first", "middle" or "last"
        '''
        if sep_type == "first":
            print(f"{TABLE_CORNER_A}{ROW_SEPARATOR * (table_width - 2)}{TABLE_CORNER_B}")
        elif sep_type == "middle":
            print(f"{COL_SEPARATOR}{ROW_SEPARATOR * (table_width - 2)}{COL_SEPARATOR}")
        elif sep_type == "last":
            print(f"{TABLE_CORNER_B}{ROW_SEPARATOR * (table_width - 2)}{TABLE_CORNER_A}")
        else:
            print("error: display row separator")

    def display_row_data(row, column_widths):
        '''Display row with data and separators.'''
        print(COL_SEPARATOR, end="")  # the first column separator

        current_column_number = 0
        for column in row:
            print(column.center(column_widths[current_column_number]), end="")
            print(COL_SEPARATOR, end="")  # the next and finally the last column separator
            current_column_number += 1
        print("")  # goes to next line

    # print_table main code
    column_widths = get_column_widths(table)
    table_width = get_table_width(column_widths)
    rows_number = len(table)

    # prints table
    display_row_separator(table_width, sep_type="first")            # ----------- first -----------
    for row_number in range(rows_number):
        display_row_data(table[row_number], column_widths)          # | row |  data  | with | sep |
        if row_number < rows_number - 1:  # do not print last one   # ----------- middle ----------
            display_row_separator(table_width, sep_type="middle")
    display_row_separator(table_width, sep_type="last")             # ------------ last -----------


def get_input(label):
    """Gets single string input from the user.

    Args:
        label: str - the label before the user prompt
    """
    return input(f"\n{label}: ")


def get_inputs(labels):
    """Gets a list of string inputs from the user.

    Args:
        labels: list - the list of the labels to be displayed before each prompt
    """
    list_of_labels = []
    for element in labels:
        element = input(f"Add {element}: ")
        list_of_labels.append(element)
    return list_of_labels


def print_error_message(message):
    """Prints an error message to the terminal.

    Args:
        message: str - the error message
    """
    print(f"\n{message}")
