#Determine the first N prime numbers using a for loop.
import math

#Reading the N value

#function is_prime(number) sqtr -> THIS WORKS
def is_prime(number: int) -> bool:
    if number <= 1 : return False
    divisor = 2
    while divisor <= math.sqrt(number):
        if(number % divisor == 0):
            #não é primo porque se é divisível por algum outro número à exceção de 1 e ele próprio
            #que se exclui se só vamos até à raiz quadrada
            return False
        divisor += 1
    
    return True



#function first_prime_from which returns the prime number for print and next iteration -> WORKS
def first_prime_from(firstNumber: int) -> int:
    firstNumber += 1 #porque ele próprio não pode ser o pŕoximo número primo a partir dele
    while is_prime(firstNumber) == False:
        firstNumber += 1
    return firstNumber


def main():
    N = int(input("N:"))
    
    n = 1
    for i in range(N):
        n = first_prime_from(n)
        print(n)


main()

    