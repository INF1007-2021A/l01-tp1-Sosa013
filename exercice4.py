import math


def calculerPosition(positionInitiale, vitesseInitiale, duree, vitesseFinale):
    # TODO faites les calculs intermediaires, vous pouvez initialiser des variables locales.
    xi = positionInitiale
    vi = vitesseInitiale
    t = duree
    vf = vitesseFinale
    # a = acceleration

    a = (vf - vi)/(t)

    # TODO calculer la position finale, assigner la valeur à la variable "positionFinale"

    positionFinale = (vi * t) + (1/2 * a * (t**2)) + xi

    return positionFinale

if __name__ == '__main__':
    positionInitiale = int(input("Entrez la position initiale en mètre: "))
    vitesseInitiale = int(input("Entrez la vitesse initiale en km/h: "))
    duree = int(input("Entrez la duree en secondes: "))
    vitesseFinale = int(input("Entrez la vitesseFinale en km/h: "))
    print(calculerPosition(positionInitiale, vitesseInitiale, duree, vitesseFinale))
