
def decomposer(secondes):

    # TODO: Assigner à la variable "annees" le nombre d'années
    annees = 3.17098*(10**-8) * secondes

    # TODO: Assigner à la variable "semaines" le nombre de semaines restantes
    semaines = 1.6534*(10**-6) * secondes

    # TODO: Assigner à la variable "jours" le nombre de jours restants
    jours = 1.1574*(10**-5) * secondes

    # TODO: Assigner à la variable "heures" le nombre d'heures restantes
    heures = 2.77778*(10**-4) * secondes

    # TODO: Assigner à la variable "minute" le nombre de minutes restantes
    minutes = 1.66667*(10**-2) * secondes

    # TODO: Assigner à la variable "secondes" le nombre de secondes restantes
    secondes = (60*60*24*7)*semaines

    # TODO: Afficher le nombres d'années, semaines, jours, heures, minutes et secondes
    print(annees ,semaines ,jours ,heures ,minutes ,secondes)

    return (annees ,semaines ,jours ,heures ,minutes ,secondes)

if __name__ == '__main__':
    secondes = int(input("Entrer les secondes: "))
    print(decomposer(secondes))
