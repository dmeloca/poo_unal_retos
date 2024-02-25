## Operaciones Básicas

### Descripción
Este programa permite al usuario realizar operaciones básicas (suma, resta, multiplicación, división) entre dos números. El usuario ingresa los dos operandos y el carácter de la operación deseada.

### Funciones

#### `ask_user(question: str) -> str`
Esta función solicita información al usuario mediante un mensaje y retorna la respuesta.

#### `make_operation(first_number: float, second_number: float, operation: str) -> float`
Esta función realiza la operación especificada entre los dos números dados. Admite los siguientes caracteres para la operación: '+', '-', '*', '/'.

#### `main() -> None`
La función principal `main` solicita al usuario los valores y la operación, los convierte a números de punto flotante y luego llama a `make_operation` para realizar la operación. Finalmente, imprime el resultado.

### Uso
Ejecute el programa y siga las instrucciones para ingresar los valores y la operación deseada.

