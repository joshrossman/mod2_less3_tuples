#3. Mastering Tuple Packing and Unpacking in Python
#Objective: The goal of this assignment is to deepen your 
# understanding of tuple packing and unpacking in Python.
# Task 1: Customer Order Processing Refine your skills in tuple unpacking 
# by managing customer orders.
# Problem Statement: You are given a list of tuples, 
# each representing a customer's order. 
# Each tuple contains the customer's name, 
# the product ordered, and the quantity. 
# Your task is to unpack each tuple and print the order details in a user-friendly format.


orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),    
]

def check_input(my_input, input_checker, my_item):
    while True: 
        try:
            my_input=int(my_input)
            if my_input<0:
                my_input=''
        except:
            pass
        if type(my_input)==input_checker and len(str(my_input))!=0:
            return my_input
            break
        else:
            if input_checker==int:
                my_input=input("Not a valid input! Input a valid quantity:  ")
                continue
            elif input_checker==str:
                if my_item==True:   
                    my_input=input("Not a valid input! Input a valid name:  ")
                else:
                    my_input=input("Not a valid input! Input a valid product:  ")
                continue
def add_order():
    cust_name=check_input(input("Customer name:"),str, True)
    item_order=check_input(input("Item Order:"),str, False)
    item_quant=check_input(input("Quantity:"),int, False)
    orders.append((cust_name,item_order,item_quant))
    for list in orders:
        print(type(list))
    print("You order has been added!")
    
def print_orders():
    for my_order in orders:  
        order_first,order_middle, order_last=my_order
        print(f"Name:{order_first}\nItem:{order_middle}\nAmount:{order_last}\n")
while True:
    user_choice=input("What would you like to do? [A]dd an order, [P]rint orders, or [E]xit?")
    if user_choice.lower()=="a" or user_choice.lower()=="add" or user_choice.lower()=="add an order":
        add_order()
    elif user_choice.lower()=="p" or user_choice.lower()=="print" or user_choice.lower()=="print orders":
        print_orders()
    elif user_choice.lower()=="e" or user_choice.lower()=="exit":
        print("Have a great day!")
        break
    else:
        print("Not a valid choice!")
        
    
    
        
        



