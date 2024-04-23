"""entre dos números, según la elección del usuario, la forma de entrada de la función será los
 dos operandos y el caracter usado para la operación. entrada: (1,2,"+"), salida (3)."""
class NoneError(Exception):
	   	def __init__(self, message):
	   		super().__init__(message)
    	

def make_operation(first_number:float,second_number:float,operation:str) -> float:
    operations =['+', '-', '*', '/']
    if operation not in operations:
    	raise NoneError("None")
    		
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
    except UnboundLocalError as error:
    	print(f"{error}")
    except ValueError:
    	print("Ingrese valores numericos")
    except NoneError:
    	print(f"{operation} no es una operación programada")
    
    

if __name__ == "__main__":
    main()