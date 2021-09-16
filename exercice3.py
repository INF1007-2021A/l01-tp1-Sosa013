
def decomposer(secondes):

    # TODO: Assigner à la variable "annees" le nombre d'années
    annees = secondes // (60*60*24*365)
    secondes_restantes01 = secondes - (annees * (60*60*24*365))

    # TODO: Assigner à la variable "semaines" le nombre de semaines restantes
    semaines = secondes_restantes01 // (60*60*24*7)
    secondes_restantes02 = secondes_restantes01 - (semaines * (60*60*24*7))

    # TODO: Assigner à la variable "jours" le nombre de jours restants
    jours = secondes_restantes02 // (60*60*24)
    secondes_restantes03 = secondes_restantes02 - (jours * (60*60*24))

    # TODO: Assigner à la variable "heures" le nombre d'heures restantes
    heures = secondes_restantes03 // (60*60)
    secondes_restantes04 = secondes_restantes03 - (heures * (60*60))

    # TODO: Assigner à la variable "minute" le nombre de minutes restantes
    minutes = secondes_restantes04 // (60)
    secondes_restantes05 = secondes_restantes04 - (minutes * (60))

    # TODO: Assigner à la variable "secondes" le nombre de secondes restantes
    secondes = secondes_restantes05
    secondes_restantes5 = secondes_restantes05

    # TODO: Afficher le nombres d'années, semaines, jours, heures, minutes et secondes

    print (annees ,semaines ,jours ,heures ,minutes ,secondes)

    return (annees ,semaines ,jours ,heures ,minutes ,secondes)

if __name__ == '__main__':
    secondes = int(input("Entrer les secondes: "))
    print(decomposer(secondes))
