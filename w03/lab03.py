# 1. Name: 
#    Celeste George
# 2. Assignment Name: 
#    Lab 03: Monoploy Design
# 3. Assignment Description:
#    Write a program that will ask the user a series of questions and 
#    determine whether the player can place a hotel on Pennslyvannia Avenue.    
# 4. What was the hardest part? Be as specific as possible.
#    
# 5. How long did it take for you to complete the assignment?
#    2.5 hours

import sys;

def main():

    # Check if the player owns all the green properties
    color = input("Do you own all the green properties? (y/n): ").lower()
    if color == 'n':
        # out: no properties
        print("\nYou cannot purchase a hotel until you own all the properties of a given color group.\n")
        sys.exit()

    # Prompt the user for the current status of properties
    pa = int(input("What is on Pennsylvania Avenue? (0:nothing, 1:one house, ... 5:a hotel): "))
    nc = int(input("What is on North Carolina Avenue? (0:nothing, 1:one house, ... 5:a hotel): "))
    pc = int(input("What is on Pacific Avenue? (0:nothing, 1:one house, ... 5:a hotel): "))
    
    # Prompt the user for available quantities
    houses = int(input("\nHow many houses are there to purchase?: "))
    hotels = int(input("How many hotels are there to purchase?: "))
    cash = int(input("How much cash do you have to spend?: "))
    
    # Determine path and provide the corresponding output
    if pa == 5:
        # out: one hotel
        print("\nYou cannot purchase a hotel if the property already has one.")
        sys.exit()
    elif pa == 4:
        if hotels >= 1:
            price = 200
            print(f"This will cost ${price}.")
            print(f"Purchase 1 hotel and {houses} house(s).")
            print("Put 1 hotel on Pennsylvania and return any houses to the bank.")
            if nc > 0:
                print(f"Put {houses} house(s) on North Carolina.")
            if pc > 0:
                print(f"Put {houses} house(s) on Pacific.")
        else:
            print("\nThere are not enough hotels available for purchase at this time.")
    elif pa < 4:
        if houses > 0:
            print("\nYou must have four houses on Pennsylvania Avenue to purchase a hotel.")
        else:
            # out: cash
            print("\nYou do not have sufficient funds to purchase a hotel at this time.")
            sys.exit()

if __name__ == "__main__":
    main()