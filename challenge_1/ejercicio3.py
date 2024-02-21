'''Escribir una función que reciba una lista de números y devuelva solo aquellos que son primos.
 La función debe recibir una lista de enteros y retornar solo aquellos que sean primos.'''

def prime(number: int) -> bool:
    divisors = []
    for divisor in range(int((number)**(1/2)), 1, -1):
        if (number % divisor) == 0:
            divisors.append(divisor)
    return len(divisors) == 0 and number > 1

def ask_user(question: str) -> str:
    return input(question)

def main():
    number_str = ask_user("[?] Ingrese los números que desea verificar: [Ejemplo:1 2 3 4 5 6 7] ")
    number_list = [int(x) for x in number_str.split() if x.isdigit()]
    
    prime_list = [number for number in number_list if prime(number)]
    
    print("Números primos:", prime_list)

if __name__ == '__main__':
    main()
