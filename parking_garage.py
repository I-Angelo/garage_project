from classes import parkingGarage
import time
import os



parking_spaces_available = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
new_ticket = parkingGarage(1, parking_spaces_available)

def run():
    os.system('clear')
    flag = True
    while flag:
        os.system('clear')
        print('\n\n\n')
        print(f"Welcome to our parking . There is a flat rate of $5.00\n\n".center(100))
        response = input('Do you want to take a ticket for parking your vehicle (y/n) or pay your ticket (p)? y/n/p \n ---> ')
        
        if response.lower() == 'y':
            new_ticket.takeTickets()
            print(f'\n\nThank you , you can now proceed to your assigned spot ......!\n\n'.center(100))
        elif response.lower() == 'n':
            os.system('clear')
            print(f'Sorry you dont want to stay. See you next time!\n\n'.center(100))
            flag = False
        elif response == 'p':
            new_ticket.payForParking()
        else:
            print('Try another command\n')
                  
run()