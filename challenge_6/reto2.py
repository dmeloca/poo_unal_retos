"""Realice una función que permita validar si una palabra es un palíndromo. 
Condición: No se vale hacer slicing para invertir la palabra y verificar que sea igual a la original."""

class VoidWord(Exception): # Create an exception when no word entered
    def __init__(self, message: str="Void word") -> None:
        super().__init__(message)

class DigitWord(Exception): # Create an exception when a number is entered
    def __init__(self, message: str="Digit Word") -> None:
        super().__init__(message)

def ask_user(question:str) -> str: # Define a function to ask user and check the correct input
    answer: str = input(question)
    if answer == '':
        raise VoidWord()
    elif answer.isdigit():
        raise DigitWord()
    else:
        return answer

def remove_accents(word: str) -> str: # Remove accents when needed
    # Define mappings of accented characters to their unaccented counterparts
    accent_map = {
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
        'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U',
        'à': 'a', 'è': 'e', 'ì': 'i', 'ò': 'o', 'ù': 'u',
        'À': 'A', 'È': 'E', 'Ì': 'I', 'Ò': 'O', 'Ù': 'U',
        'â': 'a', 'ê': 'e', 'î': 'i', 'ô': 'o', 'û': 'u',
        'Â': 'A', 'Ê': 'E', 'Î': 'I', 'Ô': 'O', 'Û': 'U',
        'ã': 'a', 'õ': 'o', 'ñ': 'n',
        'Ã': 'A', 'Õ': 'O', 'Ñ': 'N',
        'ä': 'a', 'ë': 'e', 'ï': 'i', 'ö': 'o', 'ü': 'u',
        'Ä': 'A', 'Ë': 'E', 'Ï': 'I', 'Ö': 'O', 'Ü': 'U',
        'ç': 'c', 'Ç': 'C',
    }
    
    # Remove accents from the word
    cleaned_word = ''.join(accent_map.get(char, char) for char in word)
    
    return cleaned_word

def invert_string(word:str) -> list: # The function to invert word
    word:list= [x for x in word]
    inverted_word:list=[]
    i:int = 0
    while i <= len(word)-1:
        inverted_word.append(word[(len(word)-1)-i])
        i += 1
    return inverted_word

def check_palindrome(word:str, inverted_word:list) -> str: # Function that checks if a word is a palindrome
    letter: int = 0
    while letter<=(len(word)-1):
        if word[letter] != inverted_word[letter]:
            print("[x] No es palíndromo")
            exit(0)
        else:
           letter += 1
    print("[✓] Es palíndromo")

def main(): # Main function
    try:
        word:str = ask_user("[?] Ingrese la palabra que desea comprobar: [Ejemplo: Calculadora] ")
        word = remove_accents(word.lower())
        inverted_word = invert_string(word)
        check_palindrome(word, inverted_word)
    except VoidWord:
        print("[!] Ingrese una palabra")
    except DigitWord:
        print("[!] Ingrese una palabra")        
    

if __name__=="__main__": 
    main()
