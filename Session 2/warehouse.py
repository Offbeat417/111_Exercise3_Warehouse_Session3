from item import Item
from menu import _print_menu
import datetime
import pickle
import os

logs = []
items = []
id_count = 1
header = "this is a header"
items_file = "item.data"
logs_file = "logs.data"

def clear():
    return os.system("cls")

def get_time():
    current_date = datetime.datetime.now()
    time = current_date.strftime("%X")
    return time

def save_items():
    #open creates/open a file
    #wb = write binary info
    writer = open(items_file, "wb")
    #converts the object into binary and writes it on the file
    pickle.dump(items, writer)
    writer.close() #closes the file stream (to release the file)
    print(" ** Saved: Data ** ")

def save_log():
    writer = open(logs_file, "wb")
    pickle.dump(logs, writer)
    writer.close()
    print(" ** Saved: Logs ** ")

def read_items():
    global id_count #import variable into fn scope

    try:
        reader = open(items_file, "rb") #rb = open the file to read binary
        temp_list = pickle.load(reader)

        for item in temp_list:
            items.append(item)
        
        last = items[-1]
        id_count = last.id + 1
        print(" Loaded: " + str(len(temp_list)) + "items")
    except:
        #you wind up here if the try crashes
        print("**** Error: Data could not be loaded ****")


#Functions : header_text, print_header, and print_all are added in by me, these are temps so that errors are not thrown.

def read_log():
    try:
        reader = open(logs_file, "rb") #rb = open file to Read Binary
        #Read the binary and convert it to the original object
        temp_list = pickle.load(reader)

        for log in temp_list:
            logs.append(log)
        
        print(" Loaded: " + str(len(temp_list)) + " log events")
    
    except:
        #you get here if try block crashes
        print(" ** Error: Data could not be loaded! **")




def header_text():
    print("This is the Header Text line 13")

def print_header(text):
    print("\n\n")
    print("*" * 40)
    print(text)
    print("*" * 40)


def print_all(header_text):
    print_header(header_text)
    print("*" * 70)
    print("ID   | Item Title  | Category     | Price       | Stock")
    print("*" * 70)

    for item in items:
        print(str(item.id).ljust(3) + " | " + item.title.ljust(25) + " | " + item.category.ljust(15) + " | " + str(item.price).rjust(9) + " | " + str(item.stock).rjust(5))

#Again, all the functions above are added in by me, purley for no errors
#DO NOT KEEP THESE, THEY WILL EVENTUALLY NEED TO BE REPLACED WITH
#MORE USEFUL FUNCTIONS

def register_item():
    global id_count

    print_header("Register New Item")
    title = input("Please input the title: ")
    category = input("Please input the category: ")
    price = float(input("Please input a price: "))
    stock = int(input("Please input the stock: "))

    #validations
    new_item = Item()
    new_item.id = id_count
    new_item.title = title
    new_item.category = category
    new_item.price = price
    new_item.stock = stock
    id_count += 1
    items.append(new_item)
    print(" Item Created!! ")


def update_stock():
    print_all("choose an ID to update its stock: ")
    id = input("\n select an id to update the stock")
    found = False
    for item in items:
        if(str(item.id) == id):
            stock = input("please input new stock value")
            item.stock = int(stock)
            found = True

            #add registry to the log NOT NEEDED NOW, WILL ADD LATER
            # log_line = get_time() + " | Update |" + id
            # logs.append(log_line)
            # save_log()
    if(not found):
        print("** Error: ID doesn't exist, try again **")


def print_stock_value():
    total = 0.0
    for item in items:
        total += (item.price * float(item.stock))
    
    print("Total Stock Value: " + str(total))


#read previous data form the file to items array
# read_items()   < ---NEEDED AT SOME POINT
# read_log()


#meat and potatoes
opc = ""
while(opc != "x"):
    _print_menu()
    opc = input("Select an option: ")
    if(opc == "x"):
        break
    
    elif(opc == '1'):
        register_item()
        save_items()
    elif(opc == '2'):
        print_all(header_text)
        print(items)
        save_items()
    elif(opc == '3'):
        stock_up = update_stock()
        print("Stock updated for: " + str(stock_up))
        save_items()
    # elif(opc == '4'):
    #     list_no_stock()
    # elif(opc == '5'):
    #     remove_items()
    #     save_items()
    # elif(opc == '6'):
    #     print_categories()
    elif(opc == '7'):
        print_stock_value()
    # elif(opc == '8'):
    #     register_purchase()
    # elif(opc == '9'):
    #     register_sell()
    # elif(opc == '10'):
    #     print_log()

    if(opc != "x"):
        input("\n\nPress Enter to coninue...")