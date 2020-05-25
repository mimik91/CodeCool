""" Sales module

Data table structure:
    - id (string)
    - customer id (string)
    - product (string)
    - price (float)
    - transaction date (string): in ISO 8601 format (like 1989-03-21)
"""

DATAFILE = "model/sales/sales.csv"
HEADERS = ["Id", "Customer", "Product", "Price", "Date"]


from model import data_manager, util



#------------------Geting one column--------------
def column_from_table(column_nr):
    table=data_manager.read_table_from_file(DATAFILE, separator=';')
    column=[]
    for raw in table:
        column.append(raw[column_nr])
    return column


#-----------------Biggest revenue transaction------
def max_revenue():
    table=data_manager.read_table_from_file(DATAFILE, separator=';')
    revenue_list=column_from_table(HEADERS.index("Price"))
    float_revenue=srt_to_float_list(revenue_list)
    position_of_max_revenue=float_revenue.index(max(float_revenue))
    return table[position_of_max_revenue]


#---------------Best earning product---------------
def best_total_revenue():
    table=data_manager.read_table_from_file(DATAFILE, separator=';')
    revenue_list=column_from_table(HEADERS.index("Price"))
    product_list=column_from_table(HEADERS.index("Product"))
    float_revenue=srt_to_float_list(revenue_list)
#---------------Making dictionary with products and its revenue
    total_revenue={}
    used_products=[]
    for product in product_list:
        if product not in used_products:
            total_revenue[product]=float_revenue[product_list.index(product)]
            used_products.append(product)
        else:
            total_revenue[product]=total_revenue[product]+float_revenue[product_list.index(product)]
#---------------Searching for max revenue product and returning it
    for used_product in used_products:
        if total_revenue[used_product]==(max(total_revenue.values())):
            return used_product, max(total_revenue.values())


#-------------Transactions between two given dates---
def transaction_in_period(date1, date2):
    table=data_manager.read_table_from_file(DATAFILE, separator=';')
    date_list=column_from_table(HEADERS.index("Date"))
    good_dates=[]
    #---------choosing dates between date1 and date2
    for date in date_list:
        if date>date1 and date<date2:
            good_dates.append(date)
    return good_dates


def count_transactions(date1, date2):
    transactions_dates = transaction_in_period(date1, date2)
    transactions_amount=len(transactions_dates)
    return transactions_amount


def revenue_in_dates(date1, date2):
    table=data_manager.read_table_from_file(DATAFILE, separator=';')
    transactions_dates = transaction_in_period(date1, date2)
    revenue_in_period=0
    for n in range(0, len(table)):
        if table[n][4] in transactions_dates:
            revenue_in_period=revenue_in_period+float(table[n][3])
    return revenue_in_period




def srt_to_float_list(str_list):
    float_list = []
    for record in str_list:
        float_list.append(float(record))
    return float_list


def create_item(Id, Customer, Product, Price, Date):
    table=data_manager.read_table_from_file(DATAFILE, separator=';')
    new_item=[Id, Customer, Product, Price, Date]
    table = table + [new_item]
    data_manager.write_table_to_file(DATAFILE, table, separator=';')
    return table


def read_record():
    table=data_manager.read_table_from_file(DATAFILE, separator=';')
    return table

def remove_record(record_id):
    table=data_manager.read_table_from_file(DATAFILE, separator=';')
    for n in range(0, len(table)):
        if table[n][0] == record_id:
            del table[n]
    data_manager.write_table_to_file(DATAFILE, table, separator=';')
    return table  


def modify_item(record_id, Customer, Product, Price, Date):
    table=data_manager.read_table_from_file(DATAFILE, separator=';')
    for n in range(0, len(table)):
        if table[n][0] == record_id:
            table[n]=[record_id, Customer, Product, Price, Date]
            print(table)
    data_manager.write_table_to_file(DATAFILE, table, separator=';')
    return table