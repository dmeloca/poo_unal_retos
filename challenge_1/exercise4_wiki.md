## Encontrar la Suma Máxima de Números Consecutivos

### Descripción
Este programa solicita al usuario una lista de números y encuentra la suma máxima de números consecutivos en esa lista. Utiliza una función `check_sumatory` que recorre la lista y compara las sumas de números consecutivos, actualizando la suma máxima cuando encuentra una mayor.

### Funciones

#### `ask_user(question: str) -> str`
Esta función solicita información al usuario mediante un mensaje y retorna la respuesta.

#### `check_sumatory(numbers: list) -> int`
Esta función toma una lista de números como entrada y devuelve la suma máxima de números consecutivos en esa lista. Itera sobre la lista extrayendo parejas de números y actualiza la suma máxima cuando encuentra una suma consecutiva mayor.

#### `main() -> None`
La función principal `main` solicita al usuario los números que desea verificar, convierte la entrada en una lista de enteros y encuentra la suma máxima utilizando la función `check_sumatory`. Finalmente, imprime la suma máxima.

### Uso
Ejecute el programa y siga las instrucciones para ingresar los números que desea verificar.

