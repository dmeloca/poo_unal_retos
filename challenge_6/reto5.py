"""Escribir una función que reciba una lista de string y retorne unicamente aquellos elementos que tengan los mismos caracteres.
e.g. entrada: ["amor", "roma", "perro"], salida ["amor", "roma"]"""

class VoidInput(Exception):
    def __init__(self, message:str="Void Input") -> None:
        super().__init__(message)

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

def ask_user(question: str) -> list:
    answer = input(question)
    if answer == '':
        raise VoidInput
    else:
        return remove_accents(answer).split(" ")
    
def are_anagrams(word1, word2):
    return sorted(word1) == sorted(word2)



def find_anagrams(words):
    anagram_list = []
    seen_words = set()

    for word in words:
        if word not in seen_words:
            anagram_set = {w for w in words if are_anagrams(word, w)}
            if len(anagram_set) > 1:
                anagram_list.extend(anagram_set)
            seen_words.update(anagram_set)

    return anagram_list

def main():
    try:
        word_list = ask_user("ingrese las palabras: [eg. amor roma perro] ")
        anagram_list = find_anagrams(word_list)
        print(anagram_list)
    except VoidInput:
        print("[!] Ingrese valores")
    except ValueError as error:
        print(f"{error}")

if __name__ == "__main__":
    main()
