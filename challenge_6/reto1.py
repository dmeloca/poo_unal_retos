class NoneError(Exception):
    def __init__(self, message):
        super().__init__(message)

def make_operation(first_number:float, second_number:float, operation:str) -> float:
    operations = ['+', '-', '*', '/']
    if operation not in operations:
        raise NoneError("None")
    else:
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
    try:
        first_number, second_number, operation = input("Ingrese los valores y la operación que desea usar (+,-,*,/): [ejemplo:1 2 +] ").split(" ")
    except ValueError:
        print("Ingrese tres valores")
    try:
        first_number = float(first_number)
        second_number = float(second_number)
        print(make_operation(first_number, second_number, operation))
    except UnboundLocalError:
        print("Error, no ha proporcionado un valor")
    except ValueError:
        print("Ingrese valores numericos")
    except NoneError:
        print("La operación ingresada no ha sido programada")

if __name__ == "__main__":
    main()
