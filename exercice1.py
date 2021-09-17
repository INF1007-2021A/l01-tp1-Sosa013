def fizzBuzz(n):
    # TODO imprimer la chaine de caractère appropriée avec la fonction print().
    #  Assigner ensuite la valeur à la variable resultat
# Exercice 1

    if (n % 3 == 0) and (n % 5 == 0):
        resultat = "FizzBuzz"
        return resultat

    elif n % 3 == 0 :
        resultat = "Fizz"
        return resultat


    elif n % 5 == 0 :
        resultat = "Buzz"
        return resultat

    else:
        resultat = n
        return resultat

if __name__ == '__main__':
    n = int(input("indiquez le nombre: "))
    print(fizzBuzz(n))
