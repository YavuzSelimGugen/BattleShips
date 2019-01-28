from PlayerMap import PlayerMap
from Ship import Ship
import os
import time
#--- Functions----
def clear():
    #print("\033[H\033[J")
    os.system('cls' if os.name == 'nt' else 'clear')
    #print(''*80)
def menu():
    print(""" MENU 
    1- Oyuna Basla
    2- Cikis""")

def getInputsFromPlayer(player1,shipType):
    while True:
        try:
            xCoord = int(input("X koordinati\n"))
            yCoord = int(input("Y koordinati\n"))
            print("Geminin yonunu berlirleyin\n")
            direc = input("Gecerli girdiler: (K-G-D-B)")
            ship = Ship(shipType, direc)
            player1.setShip(xCoord, yCoord, ship.fieldSize, direc)
            clear()
            player1.printForMe()
            break
        except:
            print ("Yanlis giris yaptiniz lutfen tekrar deneyiniz")

def placeMap(player1):
    print("Amiral Gemisini yerlestiriyorsunuz. Geminin burnunun hangi koordinatlarda olacagina karar verin:\n")
    getInputsFromPlayer(player1, "battleship")

    print("2 adet Kruvazor Gemisini yerlestiriyorsunuz. Geminin burnunun hangi koordinatlarda olacagina karar verin:\n")
    for i in range(2):
        getInputsFromPlayer(player1, "cruiser")

    print("3 adet Muhrip Gemisini yerlestiriyorsunuz. Geminin burnunun hangi koordinatlarda olacagina karar verin:\n")
    for i in range(3):
        getInputsFromPlayer(player1, "destroyer")

    print("4 adet Denizalti Gemisini yerlestiriyorsunuz. Geminin burnunun hangi koordinatlarda olacagina karar verin:\n")
    for i in range(4):
        getInputsFromPlayer(player1, "submarine")

def startGame():
    xCoord = 0
    yCoord = 0
    direc = ''
    print("1. oyuncu icin ad giriniz: ")
    name = input()
    player1 = PlayerMap(name)
    print("2. oyuncu icin ad giriniz: ")
    name = input()
    player2 = PlayerMap(name)
    clear()
    print("Gemi Yerlestirme Ekrani")
    player1.printForMe()
    placeMap(player1)
    time.sleep(3)
    clear()
    print("Ikinci oyuncu icin gemi yerlestime ekrani")
    player2.printForMe()
    placeMap(player2)

    while(player1.damage != 20 or player2.damage != 20):
        clear()
        print(player1.name+" atis yapiyor: \n")
        player2.printForEnemy()
        while True:
            try:
                x = int(input("X"))
                y = int(input("Y"))
                player2.fire(x, y)
                break
            except:
                print("Yanlis giris yaptiniz. Tekrar deneyiniz")
        counter = 0
        for col in player1.board:
            for row in col:
                for item in row:
                    if item != 'O':
                        counter += 1
                        if counter == 100:
                            player1.damage = 20
                    else:
                        break
        counter = 0
        for col in player2.board:
            for row in col:
                for item in row:
                    if item != 'O':
                        counter += 1
                        if counter == 100:
                            player2.damage = 20
                    else:
                        break
        if player2.damage == 20:
            clear()
            print(player1.name + " Kazandi")
            break
        clear()
        print(player2.name + " atis yapiyor: \n")
        player1.printForEnemy()
        while True:
            try:
                x = int(input("X"))
                y = int(input("Y"))
                player1.fire(x, y)
                break
            except:
                print("Yanlis giris yaptiniz. Tekrar deneyiniz")
        if player1.damage == 20:
            clear()
            print(player2.name + " Kazandi!!!")
            break








#---Main Program


userChoice = 1
while(userChoice != 2):
    menu()
    userChoice = input("Seciminizi giriniz...")
    if userChoice == '1':
        clear()
        startGame()
    elif userChoice == '2':
        exit(0)
    else:
        print("Dogru girdi giriniz.")






