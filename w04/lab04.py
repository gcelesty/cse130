# 1. Name: 
#    Celeste George
# 2. Assignment Name: 
#    Lab 04: Monoploy Program
# 3. Assignment Description:
#    Write a program that will ask the user if they are able to build a hotel
#    on Pennsylvania Avenue by asking a series of questions whether a hotel
#    can be purchased for Pennsylvania and how much it will cost.
# 4. What was the hardest part? Be as specific as possible.
#    
# 5. How long did it take for you to complete the assignment?
#    2.5 hours

import sys;

def main():
    houses_needed = []
    prices = []

    # Check if the player owns all the green properties
    color = input("Do you own all the green properties? (y/n): ").lower()
    if color == 'n':
        # out: no properties
        print("\nYou cannot purchase a hotel until you own all the properties of a given color group.\n")
        sys.exit()

    if color == "y":
        prompt_pa = int(input("\nWhat is on Pennsylvania Avenue? (0:nothing, 1:one house, ... 5:a hotel) "))
        if prompt_pa == 0:
            houses_needed.append(4)
            prices.append(800)
        elif prompt_pa == 1:
            houses_needed.append(3)
            prices.append(600)
        elif prompt_pa == 2:
            houses_needed.append(2)
            prices.append(400)
        elif prompt_pa == 3:
            houses_needed.append(1)
            prices.append(200)
        elif prompt_pa == 4:
            houses_needed.append(0)
            prices.append(0)

        # if the user answers with a response of 0-4, prompt user for the items on
        #   North Caroline Avenue 0-5
        if prompt_pa in range(0,5):
            prompt_nc = int(input("\nWhat is on North Carolina Avenue? (0:nothing, 1:one house, ... 5:a hotel) "))
            if prompt_nc == 0:
                houses_needed.append(4)
                prices.append(800)
            elif prompt_nc == 1:
                houses_needed.append(3)
                prices.append(600)
            elif prompt_nc == 2:
                houses_needed.append(2)
                prices.append(400)
            elif prompt_nc == 3:
                houses_needed.append(1)
                prices.append(200)
            elif prompt_nc == 4:
                houses_needed.append(0)
                prices.append(0)

        # if the user answers with a response of 0-4, prompt the user for the items on
        #   Pacific Avenue 0-5
            if prompt_nc in range(0,5):
                prompt_pc = int(input("\nWhat is on Pacific Avenue? (0:nothing, 1:one house, ... 5:a hotel) "))
                if prompt_pc == 0:
                    houses_needed.append(4)
                    prices.append(800)
                elif prompt_pc == 1:
                    houses_needed.append(3)
                    prices.append(600)
                elif prompt_pc == 2:
                    houses_needed.append(2)
                    prices.append(400)
                elif prompt_pc == 3:
                    houses_needed.append(1)
                    prices.append(200)
                elif prompt_pc == 4:
                    houses_needed.append(0)
                    prices.append(0)

                # if the user answers with a response of 0-4, prompt the user for the number of hotels available for purchase
                if prompt_pc in range(0,5):
                    hotels = int(input("\nHow many hotels are there to purchase? "))

                    # if the user answers anything greater than 0, calculate the number of houses the user need to buy along with the price of the houses 
                    total_cash_needed = sum(prices) + 200
                    total_houses_needed = sum(houses_needed)
                    if hotels > 0:
                        cash = int(input("\nHow much cash do you have to spend? "))

                        # if the user's current amount is greater than the total amount needed to buy all the houses and hotels, prompt the user for the number of houses available of purchase
                        if cash >= total_cash_needed:
                            houses = int(input("\nHow many houses are there to purchase? "))

                            # if the user answer anything greater than 0, show the user the total amount needed and the total nyumber of houses needed
                            if houses > 0:
                                print(f"\nYou need ${total_cash_needed} and you have ${cash}. \n       North Carolina Avenue needs {houses_needed[1]} house(s). \n       Pacific Avenue needs {houses_needed[2]} house(s).")
                        
                                # if both NC and PC need one or more houses, display option A
                                # out: purchase A
                                if houses_needed[1] > 0 and houses_needed[2] > 0:
                                    print(f"\nThis will cost ${total_cash_needed}. \n       Purchase 1 hotel and {total_houses_needed} house(s). \n       Put 1 hotel on Pennsylvania and return and houses to the bank. \n       Put {houses_needed[1]} house(s) on North Carolina. \n       Put {houses_needed[2]} house(s) on Pacific. \n")
                        
                                # if both NC and PC is greater than 0 and PA doesnt need any houses, display option B
                                # out: purchase B
                                elif houses_needed[1] > 0 and houses_needed[2] == 0:
                                    print(f"\nThis will cost ${total_cash_needed}. \n       Purchase 1 hotel and {total_houses_needed} house(s). \n       Put 1 hotel on Pennsylvania and return any houses to the bank. \n       Put {houses_needed[1]} house(s) on North Carolina. \n")
                        
                                # if both NC and PC is greater than 0 and NC doesnt need any houses, display option C
                                # out: purchase C
                                elif houses_needed[1] == 0 and houses_needed[2] > 0:
                                    print(f"\nThis will cost ${total_cash_needed}. \n       Purchase 1 hotel and {total_houses_needed} house(s). \n       Put 1 hotel on Pennsylvania and return any houses to the bank. \n       Put {houses_needed[2]} house(s) on Pacific. \n")

                                # if neither NC or PC need any houses, display option D
                                # out: purchase D
                                elif houses_needed[1] == 0 and houses_needed[2] == 0:
                                    print(f"\nThis will cost ${total_cash_needed}. \n       Purchase 1 hotel and {total_houses_needed} house(s). \n     Put 1 hotel on Pennsylvania and return any houses to the bank. \n")

                            # if the user answers 0, end the program telling the user that there are no houses available for purchase
                            # out: no houses
                            elif houses == 0:
                                print("\nThere are not enough houses available for purchase at this time.\n")
                                sys.exit()

                        # if the user's amount of cash is less than the total amount needed, end the program telling the user that they have insufficient funds
                        # out: cash
                        elif cash < total_cash_needed:
                            print(f"\nYou do not have sufficient funds to purchase a hotel at this time.\n")
                            sys.exit()
                
                    # if the user answers 0, end the program telling the user that there are no hotels for purchase
                    # out: no hotels
                    elif hotels == 0:
                        print(f"\nThere are not enough hotels available for purchase at this time.\n")
                        sys.exit()

                # if the the user answers 5, end the program telling the user to swap the hotel on PC with the houses on PA
                # out: swap PC
                elif prompt_pc == 5:
                    print("\nSwap Pacific's hotel with Pennsylvania's 4 houses.\n")
                    sys.exit()

            # if the user answers 5, end the program tellign the user to swap the hotel on NC with the houses on PA
            # out: swap NC
            elif prompt_nc == 5:
                print("\nSwap North Carolina's hotel with Pennsylvania's 4 houses.\n")
                sys.exit()

        # if the user answers 5, end the program telling the user that there can only be one hotel per property
        # out: one hotel
        elif prompt_pa == 5:
            print("\nYou cannot purchase a hotel if the property already has one.\n")
            sys.exit()

if __name__ == "__main__":
    main()