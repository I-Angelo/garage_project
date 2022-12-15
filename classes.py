import random
import time
import os

class parkingGarage():

    park_dict = {}
    value = 'Available'
    keys = range(1,16)
    for i in keys:
        park_dict[i] = value

    def __init__(self, ticket_taken, parking_spaces_available):
        self.ticket_taken = ticket_taken
        self.parking_spaces_available = parking_spaces_available


    def takeTickets(self):
    # - takeTicket
        os.system('clear')
        avail_s = len(self.parking_spaces_available)
        print(f'\n\nThere are currently {avail_s} spaces available....\n\n')
        print("This is the status of all spots :\n".center(100))
        for i in parkingGarage.park_dict.items():
            print(i)
        spot = random.choice(self.parking_spaces_available)
        taken_spot = []
        self.taken_spot = taken_spot
        new_spaces = self.parking_spaces_available
        while True:
            if spot in taken_spot:
                random.choice(self.parking_spaces_available)
            else:
                taken_spot.append(spot)
                new_spaces.remove(spot)
                self.avail_s = avail_s
                avail_s -= 1
                parkingGarage.park_dict[spot] = 'Parked Car/Not Paid'
                break

        print (f'\n\nIm printing your ticket...Your ticket number and spot is : ***   {spot}  ***....\n')
        time.sleep(4)
        avail_spaces = len(new_spaces)
        os.system('clear')
        print(f"This is the status of all spots :\n".center(100))
        for i in parkingGarage.park_dict.items():
            print(i)
        print(f'\nThere are {avail_spaces} spaces avaialble now\n\n')
        print('\n\nYou will be redirected momentarely....')
        self.new_spaces = new_spaces
        time.sleep(4)


    def payForParking(self):
        os.system('clear')
        print(f'\n\nLIST AND STATUS OF SPOTS\n\n'.center(100))
        for i in parkingGarage.park_dict.items():
            print(i)
        spot_to_pay = int(input('\n\nWhat spot number are you ? \n --> '))
        # flag = True
        while spot_to_pay not in self.taken_spot:
            spot_to_pay = int(input('What number spot are you ? \n -->'))
            print(self.taken_spot)

        print(f'You balance is $5.00\n')
        paid_amount = float(input(f'How much would you like to pay ? eg. 4.50 \n --->  '))
        balance = 5.00 - paid_amount
        if balance == 0:
            print('Tnank you. Bye bye!!\n\n')
            parkingGarage.park_dict[spot_to_pay] = 'Available'
            self.new_spaces.append(spot_to_pay)
            self.avail_s += 1
            print(self.new_spaces)
            timer_ct = 15 #(900 for 15 minutes)
            self.timer_ct = timer_ct
            parkingGarage.timerCountdown(self)
        elif balance > 5.00:
            print('Sorry but I have no change. Thank you for the donation. Good bye!')
            parkingGarage.park_dict[spot_to_pay] = 'Available'
            self.new_spaces.append(spot_to_pay)
            self.avail_s += 1
            for i in parkingGarage.park_dict.items():
                print(i)
            print(self.new_spaces)
        else:
            while balance < 5.00:
                remaining_balance = float(input(f'You have a remaining balance of {balance}. Please pay the remaining balance..\n --> '))
                remaining_balance = round(remaining_balance, 2)
                new_balance = float(remaining_balance + balance)
                new_balance = round(new_balance, 2)
                if new_balance > 5.00:
                    print('You paid in excess and I have no change. Good luck!\n\n')
                    parkingGarage.timerCountdown(self)
                    break

                if new_balance == 5.00:
                    os.system('clear')
                    print('\n\nThank you and have a nice day!!\n'.center(150))
                    parkingGarage.park_dict[spot_to_pay] = 'Available'
                    self.new_spaces.append(spot_to_pay)
                    self.avail_s += 1
                    for i in parkingGarage.park_dict.items():
                        print(i)
                    print(self.new_spaces)
                    time.sleep(3)
                    break                
    
    def timerCountdown(self):
        os.system('clear')
        print('\n\n\n')
        print("\n\n\n\nHave a nice dayy!! Tik....tok.....\n\n".center(150))
        while self.timer_ct:
            mins, secs = divmod(self.timer_ct, 60)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            print(timeformat, end='\r')
            time.sleep(1)
            self.timer_ct -= 1

        
        time.sleep(3)
       

   




