from functions.Position import position


def drawRightPanel():
    """
    Draw the right panel
    """
    print(position(105, 2, "L'île aux Pythons !".center(47, ' ')))
    print(position(105, 3, "-"*47))
    print(position(105, 4, "1 - Dormir"))
    print(position(105, 5, " "*40))
    print(position(105, 5, "2 - Ouvrir Inventaire"))
    print(position(105, 6, "q - Quitter"))
    for i in range(8, 20):
        print(position(105, i, ' '*47))
