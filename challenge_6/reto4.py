class VoidInput(Exception):
    def __init__(self, message:str="Void Input") -> None:
        super().__init__(message)


def ask_user(question: str) -> str:
    answer = input(question)
    if answer == '':
        raise VoidInput
    else:
        return answer

def check_sumatory(numbers: list) -> int:
    max_sum: int = 0
    for i in range(len(numbers)-1):
        if (numbers[i] + numbers[i+1]) > max_sum:
            max_sum = numbers[i] + numbers[i+1]
    return max_sum

def main():
    try:
        number_str = ask_user("[?] Ingrese los números que desea verificar: [Ejemplo:1 2 3 4 5 6 7] ")
        number_list = [int(x) for x in number_str.split() if x.isdigit()]
        print(f"La suma de los enteros más grandes es: {check_sumatory(number_list)}")
    except VoidInput:
        print("[!] Ingrese un valores")
if __name__ == "__main__":
    main()
