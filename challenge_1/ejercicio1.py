"""Crear una función que realice operaciones básicas (suma, resta, multiplicación, división)
entre dos números, según la elección del usuario, la forma de entrada de la función será los
 dos operandos y el caracter usado para la operación. entrada: (1,2,"+"), salida (3)."""

def ask_user(question:str) -> str:
    answer = input(question)
    return answer

def make_operation(first_number:float,second_number:float,operation:str) -> float:
    match operation:
        case '+':
            return first_number + second_number
        case '-':
            return first_number - second_number
        case '*':
            return first_number * second_number
        case '/':
            return first_number / second_number
        
def main() -> None:
    first_number, second_number, operation = ask_user("Ingrese los valores y la operación que desea usar (+,-,*,/): [ejemplo:1 2 +] ").split(" ")
    first_number = float(first_number)
    second_number = float(second_number)
    print(make_operation(first_number, second_number, operation))

if __name__ == "__main__":
    main()
