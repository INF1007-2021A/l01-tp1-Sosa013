def fizzBuzz(n):
    # TODO imprimer la chaine de caractère appropriée avec la fonction print().
    #  Assigner ensuite la valeur à la variable resultat
# Exercice 1

    if n % 3 == 0 :
        print("fizz est un multiple de 3")


    if n % 5 == 0 :
        print("buzz est un multiple de 5")


    if (n % 3 == 0) and (n % 5 == 0):
        print("fizzbuzz est à la fois un multiple de 3 et 5")


    resultat = n
    return resultat

if __name__ == '__main__':
    n = int(input("indiquez le nombre: "))
    print(fizzBuzz(n))
