from random import random
from datetime import datetime

client_birthday = ["Luis", "Carlos", "Andrea", "Ana María"] ## "Base de datos" de clientes que cumplen años ese día
day_course = ["Pasta con albóndigas", "Ajiaco", "Sudado", "Vegetariano"] ## Platos del día disponibles

class MenuItem: 
    def __init__(self, name: str, price: float, method: int):
        self.name = name
        self.price = price
        self.method = method

class Dessert(MenuItem):
    def __init__(self, name: str, price: float, method: int):
        super().__init__(name, price, method)

class Beverage(MenuItem):
    def __init__(self, name: str, price: float, method: int):
        super().__init__(name, price, method)


class Appetizer(MenuItem):
    def __init__(self, name: str, price: float, method: int):
        super().__init__(name, price, method)
        

class MainCourse(MenuItem):
    def __init__(self, name: str, price: float, method: int):
        super().__init__(name, price, method)

class SpecialCourse(MenuItem):
    def __init__(self, name: str, price: float, method: int):
        super().__init__(name, price, method)

class DayCourse(MenuItem):
    def __init__(self, option: int, method: int, price: float = 10):
        name: str = day_course[option]
        super().__init__(name, price, method)


class Service(MenuItem):
    def __init__(self, price: float, method: int, tax: float = 0):
        super().__init__("Servicio", price, method)



class ClientOrder:
    def __init__(self, items: list, client: str, table: int, payment_method: str):
        self.items = items
        self.client = client
        self.table = table
        self.payment_method = payment_method

    def calculate_bill_amount(self) -> float:
        bill = sum(item.price for item in self.items)
        bill_without_discounts = bill

        if 5 <= len(self.items) < 10 and self.client not in client_birthday: ## le descuenta el 10% de la compra si lleva entre 5 y 10 platos
            bill -= (bill * (10/100))

        elif self.client in client_birthday: # Si el cliente cumple años se le da el 50% de descuento
            bill -= (bill * (50/100))
        
        taxes = bill*(8/100)  ## se calcula el 8% del impuesto a comidas
        return bill, bill_without_discounts, taxes

    def print_bill(self) -> None:
        bill, bill_without_discounts, taxes = self.calculate_bill_amount() ## se asignan los valores del método anterior
        start = datetime(2024, 1, 30) ## para generar un día para la factura
        end = datetime(2024, 5, 28)
        random_date = start + (end - start) * random()
        print("      El Buen Sabor\n       Restaurante\n  Nit 23596041-3 R SIMPLIF\n      CRA 8 #  41-29")
        print(f"  {random_date}  \n")
        for item in self.items: ## Imprime el nombre del plato y el precio de este
            spaces = 30 - len(item.name)
            item_in_bill = f"{item.name}{' '*spaces} ${item.price:.2f}"
            print(item_in_bill)
        if sum(item.method for item in self.items)/ len(self.items) == 1: ## se revisa si el cliente quiere incluir el servivio
            print(f"Servicio{' '*(30-len('Servicio'))} ${bill*(10/100):.2f}")
        if self.client in client_birthday: ## Se le da un postre de cortesia al cliente que cumple años
            print(f"Cortesia{' '*(30-len('Cortesia'))} ${0:.2f}")
        bill_without_discounts += taxes
        print("-" * len(item_in_bill))
        print(f"Total sin descuentos:{' ' * (15-len(str(bill_without_discounts)))} ${bill_without_discounts:.2f}") ## muestra el precio total
        print(f"Descuento:{' ' * (37-len(str((bill_without_discounts - bill))))} -${(bill_without_discounts - bill):.2f}") ## muestra los descuentos obtenidos
        print(f"Impuestos:{' ' * (23 - len(str(taxes)))} +${taxes:.2f}") ## le muestra los impuestos
        print(f"Total:{' ' * (42-len(str(bill+taxes)))} ${bill+taxes:.2f}") ## imprime el total de la compra
        print(f"Método de pago: {self.payment_method[0]}") ## el método de pago
        if self.payment_method[0] == "Efectivo": ## si es con efectivo le muestra las vueltas del cliente, si es con tarjeta mustra que el pago fue aceptado
            print(f"Sobrante:{' '*len(str(self.payment_method[1]-bill))}{' '*18}${self.payment_method[1]-bill:.2f}")
        elif self.payment_method[0] == "Tarjeta":
            print(f"Pago Aceptado")
    
    def __iter__(self):
        return MenuItemIterator(self.items)

class MenuItemIterator:
    def __init__(self, items):
        self.items = items
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.items):
            item = self.items[self.index]
            self.index += 1
            return item
        raise StopIteration



def main():
    drink_1 = Beverage("Hit", 20, 1)
    drink_2 = Beverage("Ginger Ale", 20, 1)
    drink_3 = Beverage("Agua", 5, 1)
    appetizer_1 = Appetizer("Pan", 5, 1)
    appetizer_2 = Appetizer("Arepas", 7, 1)
    day_course_1 = DayCourse(0, 1)
    special_course_1 = SpecialCourse("Baby Beef", 20, 1)
    special_course_2 = SpecialCourse("Churrasco", 25, 1)

    order_1 = ClientOrder([drink_1, drink_2, drink_3, appetizer_2, appetizer_1, day_course_1, special_course_1, special_course_2], "Luis", 13, ["Efectivo", 70]) ## comentar para pago con tarjeta
    #order_1 = ClientOrder([drink_1, drink_2, drink_3, appetizer_2, appetizer_1, day_course_1, special_course_1, special_course_2], "Luis", 13, ["Tarjeta"]) ## comentar para pago con Efectivo
    for item in order_1:
        name, price, method = item.name, item.price, item.method
        print(f"{name}: {price} ---> {method}")


if __name__ == "__main__":
    main()
