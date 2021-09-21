import math


def calculerPosition(positionInitiale, vitesseInitiale, duree, vitesseFinale):
    # TODO faites les calculs intermediaires, vous pouvez initialiser des variables locales.
    xi = positionInitiale#en_mètres
    vi = vitesseInitiale#en_kilomètres_par_heure
    t = duree#en_secondes
    vf = vitesseFinale#en_kilomètres_par_heure
    # a = acceleration#en_mètres_par_seconde_carrée

    a = ((vf/3.6) - (vi/3.6))/(t)

    # TODO calculer la position finale, assigner la valeur à la variable "positionFinale"

    positionFinale = ((vi/3.6) * t) + (1/2 * a * (t**2)) + xi
    #positionFinale_kilomètres = (positionFinale/1000)

    return positionFinale

if __name__ == '__main__':
    positionInitiale = int(input("Entrez la position initiale en mètre: "))
    vitesseInitiale = int(input("Entrez la vitesse initiale en km/h: "))
    duree = int(input("Entrez la duree en secondes: "))
    vitesseFinale = int(input("Entrez la vitesseFinale en km/h: "))
    print(calculerPosition(positionInitiale, vitesseInitiale, duree, vitesseFinale))
