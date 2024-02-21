def ask_user(question: str) -> str:
    return input(question)

def main():
    number_str = ask_user("[?] Ingrese los números que desea verificar: [Ejemplo:1 2 3 4 5 6 7] ")
    number_list = [int(x) for x in number_str.split() if x != " "]
    number_list.sort()
    x: int = number_list[-1]
    y: int = number_list[-2]
    print(f"La suma de los enteros más grandes es: {x+y}")

if __name__ == "__main__":
    main()