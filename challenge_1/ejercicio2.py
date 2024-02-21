"""Realice una función que permita validar si una palabra es un palíndromo. 
Condición: No se vale hacer slicing para invertir la palabra y verificar que sea igual a la original."""

def ask_user(question:str) -> str:
    return input(question)

def invert_string(word:str) -> list:
    word:list= [x for x in word]
    print(word)
    inverted_word:list=[]
    i = 0
    while i <= len(word)-1:
        inverted_word.append(word[(len(word)-1)-i])
        i += 1
    return(inverted_word)

def check_palindrome(word:str, inverted_word:list) -> bool:
    letter: int = 0
    while letter<=(len(word)-1):
        if word[letter] != inverted_word[letter]:
            print("[x] No es palíndromo")
            exit(0)
        else:
           letter += 1
           continue
    print("[!] Es palíndromo")

def main():
    word:str = ask_user("Ingrese la palabra que desea comprobar: [Ejemplo: Calculadora] [Por favor no coloque acentos (tildes)] ")
    word = word.lower()
    inverted_word = invert_string(word)
    check_palindrome(word, inverted_word)
    

if __name__=="__main__":
    main()