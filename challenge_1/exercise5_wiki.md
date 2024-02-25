## Encontrar Anagramas en una Lista de Palabras

### Descripción
Este programa solicita al usuario una lista de palabras y encuentra aquellas que son anagramas, es decir, palabras con los mismos caracteres pero en orden diferente. Utiliza una función `are_anagrams` para verificar si dos palabras son anagramas y una función `find_anagrams` para encontrar todos los anagramas en la lista.

### Funciones

#### `are_anagrams(word1: str, word2: str) -> bool`
Esta función toma dos palabras como entrada y verifica si son anagramas comparando si sus caracteres ordenados son iguales.

#### `find_anagrams(words: list) -> list`
Esta función toma una lista de palabras como entrada y encuentra los anagramas presentes en la lista. Utiliza conjuntos para evitar duplicados y actualiza un conjunto `seen_words` con las palabras ya procesadas.

#### `main() -> None`
La función principal `main` solicita al usuario una lista de palabras, llama a la función `find_anagrams` y imprime la lista de anagramas encontrados.

### Uso
Ejecute el programa y siga las instrucciones para ingresar las palabras que desea verificar.

