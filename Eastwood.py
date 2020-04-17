import os
inventory = {
    "gold coin" : 938477566,
    "rope" : 22,
    "axe" : 3}
removed_items = ["Jan","Karol", "Karol", "Mieszko", "Karol", "Karol"]
order="count,asc"
filename="import_inventory.csv"
filename2="export_inventory.csv"



def display_inventory(inventory):
    if inventory=="":
        return None
    else:
        for n in inventory:
            print (n, inventory[n],", ")


def add_to_inventory(inventory, added_items):
    for n in added_items:
        if n in inventory:
            inventory[n]=(inventory[n]+1)
        else:
            inventory[n]=1
    display_inventory(inventory) 
    return inventory


def remove_from_inventory(inventory, removed_items):
    for n in removed_items:
        if inventory[n]>1:
            inventory[n]=inventory[n]-1
        else:
            print("k")
            del inventory[n]
    return inventory


def get_max(count):
    for i in range(len(count)):
        if count[i] == max(count):
            return i


def get_items_list(inventory):
    items=[]
    for n in inventory:
        items=items+[n]
    return items


def get_count_list(inventory):
    count=[]
    for n in inventory:
        count=count+[inventory[n]]
    return count


def list_sorted(inventory):
    items=get_items_list(inventory)
    count=get_count_list(inventory)
    count_sorted=[]
    items_sorted=[]
    while count != []:
        max=get_max(count)
        count_sorted.append(count[max])
        del count[max]
        items_sorted.append(items[max])
        del items[max]
    return count_sorted, items_sorted


def get_table(items, count):
    table=[]
    print(count)
    for n in range(0,len(count)):
        table=table+[[items[n], count[n]]]
    return table



def print_table(inventory, order):
    if order=="":
        count=get_count_list(inventory)
        items=get_items_list(inventory)
        table=get_table(items, count)
    else:
        count=(list_sorted(inventory)[0])
        items=(list_sorted(inventory)[1])
        if order=="count,desc":
            table=get_table(items, count)
        elif order=="count,asc":
            table=[["", "---------"], ["Items", "Count"], ["", "---------"]]
            for n in range(0, len(count)):
                table=table+[[items[len(count)-n-1], count[len(count)-n-1]]]
    print()
    for n in table:
        if n[0]=="":
            print("---------------------")
        else:
            print((9-len(n[0]))*" "+n[0]+"|", (9-len(str(n[1])))*" "+str(n[1]))


def import_inventory(filename, inventory):
    added_items=[]
    if os.path.isfile(filename)==True:
        with open(filename, "r") as f:
            tekst=f.read()
        tekst=tekst.rstrip()
        added_items=tekst.split(",")
        print(added_items)
        print(inventory)
        add_to_inventory(inventory, added_items)
    else:
        print("File ", filename, " not found!")

def export_inventory(inventory, filename):
    if os.access(filename2, os.W_OK)==True:
        if inventory !=[]:
             f=open(filename2, "w")
             f.write(",".join(inventory))
             f.close()
    else:
        print("You don't have permission creating file ",filename2,"!")

import_inventory(filename, inventory)      






