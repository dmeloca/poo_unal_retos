## Filtrar Números Primos en una Lista

### Descripción
Este programa recibe una lista de números del usuario y filtra aquellos que son primos. Utiliza una función para verificar si un número es primo y luego aplica esta función a cada número de la lista.

### Funciones

#### `prime(number: int) -> bool`
Esta función toma un número como entrada y devuelve `True` si es primo y `False` si no lo es. Verifica si el número tiene algún divisor en el rango [raíz cuadrada de `number`, 2) y si es mayor que 1.

#### `ask_user(question: str) -> str`
Esta función solicita información al usuario mediante un mensaje y retorna la respuesta.

#### `main() -> None`
La función principal `main` solicita al usuario los números que desea verificar, convierte la entrada en una lista de enteros y filtra los números primos utilizando la función `prime`. Finalmente, imprime la lista de números primos.

### Uso
Ejecute el programa y siga las instrucciones para ingresar los números que desea verificar.

