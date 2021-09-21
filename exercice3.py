
def decomposer(secondes):

    # TODO: Assigner à la variable "annees" le nombre d'années
    annees = int(secondes / (60*60*24*365))
    secondes_restantes1 = secondes - (annees * (60*60*24*365))

    # TODO: Assigner à la variable "semaines" le nombre de semaines restantes
    semaines = int(secondes_restantes1 / (60*60*24*7))
    secondes_restantes2 = secondes_restantes1 - (semaines * (60*60*24*7))

    # TODO: Assigner à la variable "jours" le nombre de jours restants
    jours = int(secondes_restantes2 / (60*60*24))
    secondes_restantes3 = secondes_restantes2 - (jours * (60*60*24))

    # TODO: Assigner à la variable "heures" le nombre d'heures restantes
    heures = int(secondes_restantes3 / (60*60))
    secondes_restantes4 = secondes_restantes3 - (heures * (60*60))

    # TODO: Assigner à la variable "minute" le nombre de minutes restantes
    minutes = int(secondes_restantes4 / (60))
    secondes_restantes5 = secondes_restantes4 - (minutes * (60))

    # TODO: Assigner à la variable "secondes" le nombre de secondes restantes
    secondes = secondes_restantes5
    secondes_restantes6 = secondes_restantes5

    # TODO: Afficher le nombres d'années, semaines, jours, heures, minutes et secondes

    print (annees ,semaines ,jours ,heures ,minutes ,secondes)

    return (annees ,semaines ,jours ,heures ,minutes ,secondes)

if __name__ == '__main__':
    secondes = int(input("Entrer les secondes: "))
    print(decomposer(secondes))
