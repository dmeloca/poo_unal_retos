"""Escribir una función que reciba una lista de string y retorne unicamente aquellos elementos que tengan los mismos caracteres.
e.g. entrada: ["amor", "roma", "perro"], salida ["amor", "roma"]"""
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
    word_list = input("ingrese las palabras: [eg. amor roma perro]").split(" ")

    anagram_list = find_anagrams(word_list)

    print(anagram_list)

if __name__ == "__main__":
    main()
