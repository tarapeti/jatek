import time
import sys
import os
import getpass

def main():

    choice ='0'
    while choice =='0':
        print("Choose 1 of 3 choices\n")
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

def back():
    try:
        input("Press Enter to go back to main menu")
        os.system('clear')
        main()
    except SyntaxError:
        pass

def leaderboard():
    score1, score2 = 0,0
    with open('leaderboard.txt', 'r') as board:
        full = board.read()
        splitted = full.split(',')

    print(splitted)

    print(score1)
    print(score2)

def game():
    os.system('clear')
    text = open('snoblitext.txt', 'r')
    print(text.read())

    name1 = input('Player 1 adj meg egy nevet: ')
    if name1 == '':
        name1 = 'Diló'

    name2 = input('Player 2 adj meg egy nevet: ')
    if name2 == '':
        name2 = 'Bázis'


    def snobli():
    
        amount = int(input('Hány érme/ fő legyen? '))
        playerone = None
        playertwo = None
        oneguess = None
        twoguess = None

        print('\n')

        # érmerejtés
        while playerone not in range(amount + 1):
            playerone = int(getpass.getpass(
                '{0} add meg, hány érmét rejtesz el a {1}-ból: '.format(name1, amount)))

            if playerone > amount:
                print(
                    '{0}, kérlek 1 és {1} között válassz!'.format(
                        name1, str(amount)))

        print('\n')

        while playertwo not in range(amount + 1):
            playertwo = int(getpass.getpass(
                '{0} add meg, hány érmét rejtesz el a {1}-ból: '.format(name2, amount)))

            if playertwo > amount:
                print(
                    '{0}, kérlek 1 és {1} között válassz!'.format(
                        name2, str(amount)))

        print('\n')
        # tippelés

        while oneguess not in range(amount * 2 + 1):
            oneguess = int(
                input(
                    '{0}, tippeld meg hány érme van játékban: '.format(name1)))

            if oneguess > amount * 2:
                print(
                    '{0}, kérlek 1 és {1} között tippelj!'.format(
                        name1, amount * 2))

        print('\n')

        while twoguess not in range(amount * 2 + 1):
            twoguess = int(
                input(
                    '{0}, tippeld meg hány érme van játékban: '.format(name2)))

            if twoguess > amount * 2:
                print(
                    '{0}, kérlek 1 és {1} között tippelj!'.format(
                        name2, amount * 2))
            else:
                continue

        print('\n')

        # végkimenetel

        all = playerone + playertwo
        difference1 = abs(all - oneguess)
        difference2 = abs(all - twoguess)
        table = open('table.txt', 'a')
        leaderboard = open('leaderboard.txt', 'a')

        print('{0} {1} rejtett el'.format(name1, playerone))
        print('{0} {1} rejtett el'.format(name2, playertwo))
        print('\n')

        if difference1 == difference2:
            print('Döntetlen')

        elif difference1 == 0 and difference2 != 0:
            print('{0} telibe találta!'.format(name1))
            table.write(name1 + ',')
            leaderboard.write(name1 + ',')

        elif difference2 == 0 and difference1 != 0:
            print('{0} telibe találta!'.format(name2))
            table.write(name2 + ',')
            leaderboard.write(name2 + ',')


        elif difference1 < difference2 and difference1 != 0:
            print('{0} közelebb volt!'.format(name1))
            table.write(name1 + ',')
            leaderboard.write(name1 + ',')


        elif difference2 < difference1 and difference2 != 0:
            print('{0} közelebb volt!'.format(name2))
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

        print('{0} pontjai: {1}'.format(name1, points1))
        print('{0} pontjai: {1}'.format(name2, points2))

        kovi = None
        kovi = input('Szeretnétek még egyet játszani? [Y/N]')
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

def quit():
    print("Quiting the game...")
    time.sleep(2)
    print('Byebye!')
    time.sleep(2)
    os.system('clear')
    sys.exit()

def credits():
    file = open('credits.txt', 'r')
    lines = file.readlines()
    for i in lines:
        print(i)
        time.sleep(1)
    back()


main()


#kell play
#kell emoji
#clear