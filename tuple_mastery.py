"""
1. Tuple Mastery in Python
Objective: The aim of this assignment is to deepen your understanding of tuples in Python.

Task 1: Formatting Flight Itineraries Create a Python function that takes a list 
of tuples as an argument. Each tuple contains information about a flight itinerary: 
(traveler_name, origin, destination). The function should format and return a string that 
lists each itinerary. For example, if the input is `[("Alice", "New York", "London"), ("Bob", "Tokyo",
 "San Francisco")]`, the output should be a string formatted as:

"Itinerary 1: Alice - From New York to London
 Itinerary 2: Bob - From Tokyo to San Francisco"


[("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]`, the output should be a string formatted as:
"""
all_flights=[]
def gather_input(input_data):
   while True:   
        if input_data=='':
            input_data=input("No data submitted. Please input a valid name:")
        else:
            return input_data
            break
def new_flights():   
    pass_name=gather_input(input("What is the passanger's name?"))
    pass_origin=gather_input(input("What is the passanger's place of origin?"))
    pass_destination=gather_input(input("What is the passanger's destination?"))
    all_flights.append((pass_name,pass_origin,pass_destination,))
    
def print_flights():
    x=1
    if len(all_flights) ==0:
        print("No flights to print")    
    else:
        for my_list in all_flights:
            print (f"Itinerary {x}: {my_list[0]} - From {my_list[1]} to {my_list[2]}") 
            x+=1 

while True:
    user_choice=input("What would you like to do? [1]Add a flight [2]Print flights [3]Exit")
    if user_choice=="1" or user_choice.lower()=="a" or user_choice.lower()=="add" or user_choice.lower()=="add a flight":      
        new_flights()
    elif user_choice=="2" or user_choice.lower()=="p" or user_choice.lower()=="print" or user_choice.lower()=="print flights":      
        print_flights()
    elif user_choice=="3" or user_choice.lower()=="e" or user_choice.lower()=="exit":
        print("Thank you! Have a great day!")
        break
    else:
        print("Invalid Choice!")

    

        
        

#"Itinerary 1: Alice - From New York to London
# Itinerary 2: Bob - From Tokyo to San Francisco"
