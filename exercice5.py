def pointDeRencontre(v1, v2, distance):
    # TODO faites les calculs intermediaires, vous pouvez initialiser des variables locales.
    xi1 = 0
    xi2 = distance


    # TODO calculer la position de rencontre, assignez la valeur à la variable "positionRencontre"
    positionRencontre = -(v1*xi2)+(v2*xi1)/(v2-v1)
    return positionRencontre

if __name__ == '__main__':
    v1 = int(input("Entrez v1: "))
    v2 = int(input("Entrez v2: "))
    distance = int(input("Entrez la distance: "))
    print(pointDeRencontre(v1, v2, distance))
