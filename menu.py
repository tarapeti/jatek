import time
import sys
import os

def quit():
    print("Quiting the game...")
    time.sleep(2)
    print('Byebye!')
    time.sleep(2)
    os.system('clear')
    sys.exit()


def emoji_menu():
    print("""
    
    
    
    
    """)
def credits():
    file = open('credits.txt', 'r')
    lines = file.readlines()
    for i in lines:
        time.sleep(1)
        print(i)
        time.sleep(1)

def main():

    choice ='0'
    while choice =='0':
        print("Main Choice: Choose 1 of 4 choices")
        print("Choose 1 for Play")
        print("Choose 2 for Emoji")
        print("Choose 3 for Credits")
        print("Choose 4 for Quit")

        choice = input ("Please make a choice: ")

        if choice == "4":
            quit()
        elif choice == "3":
            credits()
        elif choice == "2":
            print("Do Something ")
        elif choice == "1":
            print("Do Something ")
        else:
            print("I don't understand your choice.")
        



main()