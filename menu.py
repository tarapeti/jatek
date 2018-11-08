import time
import sys
import os
import getpass
import random
from collections import OrderedDict

def back():
    try:
        input("Press Enter to go back to the main menu!")
        os.system('clear')
        main()
    except SyntaxError:
        pass

def credits():
    os.system('clear')
    file = open('credits.txt', 'r')
    lines = file.readlines()
    for i in lines:
        print(i)
        time.sleep(1)
    back()

def game():
    os.system('clear')
    text = open('snoblitext.txt', 'r')
    print(text.read())

    name1 = input('Player 1 type in a nickname: ')
    if name1 == '':
        name1 = 'Diló'

    name2 = input('Player 2 type in a nickname: ')
    if name2 == '':
        name2 = 'Bázis'

    def snobli():
        amount = random.randint(3,6)
        print('You both have {0} coins to hide. '.format(amount))
        playerone = None
        playertwo = None
        oneguess = None
        twoguess = None

        print('\n')

        # hiding the coins
        while playerone not in range(amount + 1):
            playerone = int(getpass.getpass(
                '{0}, decide how many coins you would like to hide out of {1}: '.format(name1, amount)))

            if playerone > amount:
                print(
                    '{0}, dont cheat u fkin bastard!'.format(
                        name1))

        print('\n')

        while playertwo not in range(amount + 1):
            playertwo = int(getpass.getpass(
                '{0} decide how many coins you would like to hide out of {1}: '.format(name2, amount)))

            if playertwo > amount:
                print(
                    '{0}, can u not cheat?!'.format(
                        name2))

        print('\n')
        # guessing

        while oneguess not in range(amount * 2 + 1):
            oneguess = int(
                input(
                    '{0}, guess how many coins have been hidden: '.format(name1)))

            if oneguess > amount * 2:
                print(
                    '{0}, you can guess maximum {1}!'.format(
                        name1, amount * 2))

        print('\n')

        while twoguess not in range(amount * 2 + 1):
            twoguess = int(
                input(
                    '{0}, guess how many coins have been hidden: '.format(name2)))

            if twoguess > amount * 2:
                print(
                    '{0}, you can guess maximum {1}!'.format(
                        name2, amount * 2))
            else:
                continue

        print('\n')

        # outcome

        all = playerone + playertwo
        difference1 = abs(all - oneguess)
        difference2 = abs(all - twoguess)
        table = open('table.txt', 'a')
        leaderboard = open('leaderboard.txt', 'a')

        print('{0} was hiding {1} coins.'.format(name1, playerone))
        print('{0} was hiding {1} coins.'.format(name2, playertwo))
        print('\n')

        if difference1 == difference2:
            print('Tie!')

        elif difference1 == 0 and difference2 != 0:
            print('{0} guessed it exactly right. Killed it!'.format(name1))
            table.write(name1 + ',')
            leaderboard.write(name1 + ',')
    
        elif difference2 == 0 and difference1 != 0:
            print('{0} guessed it exactly right. Killed it!'.format(name2))
            table.write(name2 + ',')
            leaderboard.write(name2 + ',')


        elif difference1 < difference2 and difference1 != 0:
            print('{0} was closer!'.format(name1))
            table.write(name1 + ',')
            leaderboard.write(name1 + ',')


        elif difference2 < difference1 and difference2 != 0:
            print('{0} was closer!'.format(name2))
            table.write(name2 + ',')
            leaderboard.write(name2 + ',')


        table.close()
        leaderboard.close()

        print('\n')

        points1 = 0
        points2 = 0

        with open('table.txt', 'r') as tabella:
            egybe = tabella.read()
            kulon = egybe.split(',')
            for i in range(len(kulon)):
                if kulon[i] == name1:
                    points1 += 1
                elif kulon[i] == name2:
                    points2 += 1

        print('{0}s points: {1}'.format(name1, points1))
        print('{0}s points: {1}'.format(name2, points2))
        print('\n')

        kovi = None
        kovi = input('Would you like to play another one? [Y/N]')
        os.system('clear')
        status = None

        if kovi == 'y':
            status = 1
        elif kovi == 'n':
            status = 0

        if status == 1:
            return status
        else:
            torles = open('table.txt', 'w')
            torles.close()
            os.system('clear')
            back()
            pass
    snobli()

    if bool(snobli()) == True:
        snobli()

def leaderboard():
    os.system('clear')
    print('Leaderboard:\n')
    board = open('leaderboard.txt', 'r')
    full = board.read()
    splitted = full.split(',')
    lead = OrderedDict({x:splitted.count(x)for x in splitted})
    lead_mod = dict(lead)
    del lead_mod['']
    lead_decr = sorted(lead_mod.items(), key=lambda t : t[1] , reverse=True)
    for key, value in lead_decr:
        print(key, value)
    back()

def quit():
    print("Quiting the game...")
    time.sleep(2)
    print('Byebye!')
    time.sleep(2)
    os.system('clear')
    sys.exit()

def main():

    choice ='0'
    while choice =='0':
        print("Choose one of the 4 choices\n")
        print("1: Play")
        print("2: Leaderboard")
        print("3: Credits")
        print("4: Quit")

        choice = input ("\nPlease make a choice: ")

        if choice == "4":
            quit()
        elif choice == "2":
            leaderboard()
        elif choice == "1":
            game()
        elif choice == "3":
            credits()
        else:
            print("I don't understand your choice.")

main()

 
#leaderboard kiírása szebben                 P
#prezentáció
#credit zene??
