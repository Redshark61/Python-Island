import json
import os
import time
from functions.Clear import clear
from functions.Colors import Colors
from functions.Position import position, printBox
from functions.translateText import translateTextUp
from functions.drawRightPanel import drawRightPanel
from functions import config
from map.mapLoop import drawFood, drawWater, drawEnergy


def introduction():

    color = Colors()
    color.init()
    clear()
    with open('./data/introduction.json', encoding='utf-8') as f:
        introData = json.load(f)

    width = os.get_terminal_size()[0]

    print("Bienvenue sur :".center(width, ' '))
    time.sleep(1)

    introMap = ''
    for i in introData:
        for j in i:
            if j == 3:
                introMap += color.setBackground('brightCyan', '  ')
            elif j == 1:
                introMap += color.setBackground('red', '  ')
            elif j == 2:
                introMap += color.setBackground('brightYellow', '  ')
        introMap += '\n'
    splitedMap = introMap.split('\n')

    for i, value in enumerate(splitedMap):
        leftStart = round((width/2)-(len(value)/6/2))
        splitedMap[i] = '\u0020'*(leftStart) + value

    translateTextUp(splitedMap, 0.2)
    time.sleep(3)

    print("Pour jouer, utilisez les flèches du clavier".center(width, ' '))
    time.sleep(4)
    clear()
    printBox(103, 1, 50, 38)
    drawRightPanel()
    print(position(10, 10, "Cette partie contient les actions possible en jeu : "))
    print(position(10, 11, "ouvrir l'inventaire, dormir, quitter ou jouer aux quêtes"))
    time.sleep(6)
    clear()

    print(position(10, 10, "Cette partie contient les informations du joueur :"))
    print(position(10, 11, "Sa faim, sa soif, son énergie et son inventaire."))
    print(position(10, 14, "Lorsque votre inventaire est plein vous ne pouvez plus prendre d'objets."))
    print(position(10, 15, "Vous pouvez simplement consommer un élément."))
    print(position(10, 17, "Si vous n'avez plus d'énergie, reposez-vous. Cela consommera de la nourriture."))
    print(position(10, 19, "Si vous manquez d'une des trois constantes, vous mourrerez"))
    printBox(1, 30, 101, 9)
    drawFood(config.vitalSigns["foodMax"])
    drawWater(config.vitalSigns["waterMax"])
    drawEnergy(config.vitalSigns["energyMax"])

    time.sleep(15)
    clear()
    print("Bon jeu".center(width, ' '))
    time.sleep(3)
    clear()
