## Verificación de Palíndromo sin Slicing

### Descripción
Este programa permite al usuario verificar si una palabra es un palíndromo sin utilizar slicing para invertir la palabra. Se solicita al usuario una palabra, la convierte a minúsculas, invierte la palabra sin utilizar slicing y verifica si es un palíndromo.

### Funciones

#### `ask_user(question: str) -> str`
Esta función solicita información al usuario mediante un mensaje y retorna la respuesta.

#### `invert_string(word: str) -> list`
Esta función toma una palabra como entrada, la convierte en una lista de caracteres y luego invierte la lista sin utilizar slicing. Retorna la lista invertida.

#### `check_palindrome(word: str, inverted_word: list) -> None`
Esta función compara la palabra original con la palabra invertida letra por letra para determinar si es un palíndromo o no.

#### `main() -> None`
La función principal `main` solicita al usuario la palabra que desea verificar, la convierte a minúsculas, invierte la palabra y verifica si es un palíndromo llamando a `check_palindrome`.

### Uso
Ejecute el programa y siga las instrucciones para ingresar la palabra que desea comprobar.

