from datetime import datetime

class MenuItem: 
    def __init__(self, name: str, price: float = 0, description: str = None):
        self._name = name
        self._price = price
        self._description = description
    
    def get_description(self):
        return self._description
    
    def get_name(self):
        return self._name
    def set_name(self, new_name):
        self._name = new_name
    def get_price(self):
        return self._price
    
    def set_price(self, new_price):
        self._price = new_price

class Beverage(MenuItem):
    def __init__(self, name: str, price: float = 0, description: str = None):
        super().__init__(name, price, description)
    def get_description(self):
        return self._description
    def set_price(self, new_price):
        self._price = new_price
    def get_price(self):
        return self._price
    def set_price(self, new_price):
        self._price = new_price

class Appetizer(MenuItem):
    def __init__(self, name: str, price: float = 0, description: str = None):
        super().__init__(name, price, description)
    def get_description(self):
        return self._description
    def set_price(self, new_price):
        self._price = new_price
    def get_price(self):
        return self._price
    def set_price(self, new_price):
        self._price = new_price

class Wildside(MenuItem):
    def __init__(self, name: str, price: float =0, description: str = None):
        super().__init__(name, price, description)
    def get_description(self):
        return self._description
    def set_price(self, new_price):
        self._price = new_price
    def get_price(self):
        return self._price
    def set_price(self, new_price):
        self._price = new_price

class Dessert(MenuItem):
    def __inti__(self, name: str, price: float = 0, description: str = None):
        super().__init__(name, price, description)
    def get_description(self):
        return self._description
    def set_price(self, new_price):
        self._price = new_price
    def get_price(self):
        return self._price
    def set_price(self, new_price):
        self._price = new_price

class BagGag(MenuItem):
    def __init__(self, name: str, price: float = 0, description: str = None):
        super().__init__(name, price, description)
    def get_description(self):
        return self._description
    def set_price(self, new_price):
        self._price = new_price
    def get_price(self):
        return self._price
    def set_price(self, new_price):
        self._price = new_price

class GuessMess(MenuItem):
    def __init__(self, name: str, price: float = 10, description: str = None):
        super().__init__(name = "Guess Mess", price = price, description = description)
    
    def check_guess(self, guess):
        if guess == "Stripped Racoon":
            return True
        else: 
            return False
        
    def get_description(self):
        return self._description
    def set_price(self, new_price):
        self._price = new_price
    def get_price(self):
        return self._price
    def set_price(self, new_price):
        self._price = new_price

class LateDelight(MenuItem):
    def __init__(self, name: str, price: float = 0, description: str = None):
        super().__init__(name, price, description)
    def get_description(self):
        return self._description
    def set_price(self, new_price):
        self._price = new_price
    def get_price(self):
        return self._price
    def set_price(self, new_price):
        self._price = new_price

class PaymentMethod:
    def __init__(self, name: str = None):
        self._name = name

    def get_payment_method(self):
        return self._name
    
    def pay(self, mount):
        pass

class Order:
    def __init__(self, menu_items: list, payment_method: PaymentMethod):
        self.__menu_items = menu_items
        self.__payment_method = payment_method

    def get_order(self):
        list_order = [item.get_name() for item in self.__menu_items]
        return list_order

    def pop_item_in_order(self, item:int = None):
        self.__menu_items.pop(item)
    
    def add_item_to_order(self, item):
        self.__menu_items.append(item)

    def calculate_items_types(self):
        items_type = {"Beverage": 0,
                      "Appetizer": 0, 
                      "BagGag": 0, 
                      "GuessMess": 0,
                      "LateDelight": 0,
                      "Dessert": 0}
        for item in self.__menu_items:
            if type(item) == Beverage:
                items_type["Beverage"] += 1
            elif type(item) == Appetizer:
                items_type["Appetizer"] += 1
            elif type(item) == BagGag:
                items_type["BagGag"] += 1
            elif type(item) == GuessMess:
                items_type["GuessMess"] += 1
            elif type(item) == LateDelight:
                items_type["LateDelight"] += 1
            elif type(item) == Dessert:
                items_type["Dessert"] += 1     
        return items_type
    
    def calculate_bill(self):
        num_items = self.calculate_items_types()
        bill_amount = 0
        for item in self.__menu_items:
            bill_amount += item.get_price()
        discounts =0
        if num_items["Beverage"] == 20:
            discounts += (bill_amount*0.1)

        elif num_items["GuessMess"] != 0:
            user_guess: str = input("[?] Try to guess the name of today's special GUESSMESS: ")
            guess_mess_index = 0
            for item in self.__menu_items:
                if type(item) == GuessMess:
                    break
                else:
                    guess_mess_index += 1
            if self.__menu_items[guess_mess_index].check_guess(user_guess):
                print("[*]That's correct, you have 100% off in your meal")
                discounts = bill_amount
                return bill_amount, discounts
            else:
                self.__menu_items[guess_mess_index].set_name("Stripped Racoon")
                print(f"Better luck next time the GUESS MESS' name was {self.__menu_items[guess_mess_index].get_name()}")

        elif num_items["Appetizer"] == 10:
            discounts += (bill_amount*0.15)
        elif num_items["BagGag"] == 5:
            discounts += (bill_amount*0.2)
        elif num_items["LateDelight"] != 0 and (datetime.now().time().hour > 22 or datetime.now().time().hour < 3):
            discounts += (bill_amount*0.5)
        elif num_items["Dessert"] == 4:
            discounts += (bill_amount*0.1)

        return bill_amount, discounts
    
    def set_payment_method(self, payment_method):
        self.payment_method = payment_method
        return None
    
    def get_payment_method(self):
        return self.payment_method.name
    
    def get_items_in_order(self):
        return self.__menu_items
    
class Card(PaymentMethod):
    def __init__(self, types: str, key: int = 0000, limit: float = 10000):
        super().__init__(name = "Card")
        self.type = types
        self.limit = limit
        self.key = key
    
    def pay(self, mount: float):
        if self.limit > mount:
            return True
        else:
            return False

class Cash(PaymentMethod):
    def __init__(self, quantity: float = 1000):
        super().__init__(name="Cash")
        self.quantity = quantity
    
    def pay(self, mount: float):
        if self.quantity >= mount:
            return True
        else: 
            return False
     
menu = [Appetizer("Center Line Bovine", 4.95, "Tastes real good - straight from the hood"),#1
                Appetizer("The Chicken", 3.95, "This one didn't cross the road"),
                Appetizer("Flat Cat", 2.95, "Served as a single - or in a stack"),
                Wildside("Chunk of Skunk", 1.95),#4
                Wildside("Smidgen of Pigeon", 1.95),
                Wildside("Shake & Bake Snake", 2.25),
                Wildside("Swirl of Squirrel", 1.55),
                Wildside("Whippoorwill on a Grill", 3.30),
                Wildside("Narrow Sparrow", 0.55),
                Wildside("Rigor Mortis Tortoise", 6.75),
                BagGag("Slab of Lab",2.95),#11
                BagGag("Pit Bull Pot Pie", 1.95),
                BagGag("Cocker Cutlets", 3.95),
                BagGag("Shar-pei Filet", 5.95),
                BagGag("Poodles-N-Noodles", 5.95),
                BagGag("Snippet of Whippet", 4.50),
                BagGag("Collie Hit by a Trolley", 3.95),
                BagGag("German Shepherd Pie", 3.95),
                BagGag("Round of Hound", 4.25),
                GuessMess(" "), #20
                LateDelight("Rack of Raccoon", 3.95),
                LateDelight("Smear of Deer", 4.95),
                LateDelight("Awesome Possum", 1.95),
                LateDelight("Cheap Sheep", 0.43),
                Beverage("Snake Shake", 1.25),#25
                Beverage("Vanilla Armidilla", 1.25, "(strained or unstrained)"),
                Beverage("Muskrat Malted.", 1.25),
                Beverage("Armadillo Sasparilla", 1.25),
                Beverage("Wind-Blade Lemonade", 1.95),
                Dessert("Frog Lime Pie", 2.25),#30
                Dessert("Road Toad Ala Mode", 1.65, "(chocolate, vanilla, or orange sherbet)"),
                Dessert("Pineapple Porcupine Split", 2.25),
                Dessert("Meadow Muffins", 1.00, "(whole wheat, corn, or alfalfa)")] #33

def print_menu():
    menu_letter_1 = '''
                 __,                     ,__
              __/==+\  ROADKILL  GRILL  /+==\__
                "  "`  ===============  '"  "

            YOU KILL IT..............WE GRILL IT!

                     "Meals Under Wheels"

                           EL MENU

      ---------------------------------------------------

                "Eating food is a lot more fun
             When you know it was hit on the run!"


                           ENTREES'''
    menu_letter_2 = '''
                  A TASTE OF THE WILD SIDE
                     (Still in the Hide)'''
    menu_letter_3 = '''
                         BAG `N' GAG

              Our daily take-out lunch special
                 - Anything Dead in Bread -

      ---------------------------------------------------

       YOU'LL EAT LIKE A HOG.....WHEN YOU TASTE OUR DOG!'''
    menu_letter_4 = '''

                      GUESS THAT MESS

                 * A Daily Special Treat *

               If you can guess what it is...
                    YOU EAT IT FOR FREE! 
                            [20]

                     LATE NIGHT DELIGHT'''
    menu_letter_5 = '''
             Served fresh each night after dark

      ---------------------------------------------------

        WASH THAT GOOD FOOD DOWN WITH SOMETHING TO DRINK'''
    menu_letter_6 = '''
      TITILLATE YOUR TASTE BUDS WITH THESE GREAT DESSERTS'''
    menu_letter_7 = '''
            In God We Trust - All Others Pay Cash or Card'''
    
    print(menu_letter_1)
    counter: int = 1
    for entree in range(0, 3):
        print(f"    [{counter}]{menu[entree].get_name()}{'.'*(50-(len(menu[entree].get_name())+len(str(menu[entree].get_price()))))}{menu[entree].get_price()}")
        print(f"        {menu[entree].get_description()}")
        counter += 1
    print(menu_letter_2)
    for wild in range(3,10):
        print(f"    [{counter}]{menu[wild].get_name()}{'.'*(50-(len(menu[wild].get_name())+len(str(menu[wild].get_price()))))}{menu[wild].get_price()}")
        counter += 1
    print(menu_letter_3)
    for wild in range(10, 19):
        print(f"    [{counter}]{menu[wild].get_name()}{'.'*(50-(len(menu[wild].get_name())+len(str(menu[wild].get_price()))))}{menu[wild].get_price()}")
        counter += 1

    print(menu_letter_4)
    counter += 1

    for delight in range(20, 24):
        print(f"    [{counter}]{menu[delight].get_name()}{'.'*(50-(len(menu[delight].get_name())+len(str(menu[delight].get_price()))))}{menu[delight].get_price()}")
        counter += 1

    print(menu_letter_5)
    
    for drink in range(24,29):
        print(f"    [{counter}]{menu[drink].get_name()}{'.'*(50-(len(menu[drink].get_name())+len(str(menu[drink].get_price()))))}{menu[drink].get_price()}")
        counter += 1
        if menu[drink].get_description() != None:
            print(f"        {menu[drink].get_description()}")

    print(menu_letter_6)

    for dessert in range(29, 33):
        print(f"    [{counter}]{menu[dessert].get_name()}{'.'*(50-(len(menu[dessert].get_name())+len(str(menu[dessert].get_price()))))}{menu[dessert].get_price()}")
        counter += 1
        if menu[dessert].get_description() != None:
            print(f"        {menu[dessert].get_description()}")

    print(menu_letter_7)

def print_bill(bill: float, discounts: float, order: Order):
    menu_letter_1 = '''
                 __,                     ,__
              __/==+\  ROADKILL  GRILL  /+==\__
                "  "`  ===============  '"  "

            YOU KILL IT..............WE GRILL IT!

                     "Meals Under Wheels"

                           YOUR BILL

      ---------------------------------------------------

                "Eating food is a lot more fun
             When you know it was hit on the run!"  '''
    print(menu_letter_1)
    for dish in order.get_items_in_order():
        print(f"{dish.get_name()}{'.'*(50-(len(dish.get_name())-len(str(dish.get_price()))))}{dish.get_price()}")
    print("      ---------------------------------------------------")
    print(f"{'Total'}{'.'*(50-(len('Total')+len(str(bill))))}{bill:.2f}")
    print(f"{'Discounts'}{'.'*(50-(len('Discounts')+len(str(bill))))}{discounts:.2f}")
    print(f"{'To Pay'}{'.'*(50-(len('To pay')+len(str(bill - discounts))))}{bill - discounts:.2f}")
    print(f"\n             We know you want to come back\n")

def main():
    print("[!] Welcome back to our Restaurant here is the menu.")
    order = Order([], None)
    print_menu()
    while True:
        user_input: str = input("[?] Insert the number asociated to de dish you want (1 to 33) or (C) if you want to confirm your order: ")
        if user_input.lower() == "c":
            break
        else:
            try:
                user_input = int(user_input)
                if int(user_input) in range(1, 34):
                    user_input -= 1
                    order.add_item_to_order(menu[user_input])
                    print(f"[*] Added {menu[user_input].get_name()} to the order")
                else:
                    print("[!] Bad number please try again")
            except ValueError:
                print("[!] Incorrect Option, please try again")
    print(f"[!] Your order is: {order.get_order()}")
    bill, discounts = order.calculate_bill()
    print_bill(bill, discounts, order)

    if bill-discounts != 0:
        while True:
            user_payment: str = input("[?] Please select a payment method (B) for cash and (C) for card ")
            if user_payment.lower() == "b":
                user_quantity = input("[?] Please insert the amount of money you assign to pay your meal  (10000 for 1K dollar and 1 for 1 dollar)  ")
                try: 
                    user_quantity = int(user_quantity)
                    cash_1 = Cash(user_quantity)
                    order.set_payment_method(cash_1)
                    if cash_1.pay(bill-discounts):
                        print(f"[*] Alright, all paid. The tip is optional. Your change is: {user_quantity-(bill-discounts):.2f}")
                        break

                except ValueError:
                    print("[!] Please insert a correct value ")
                
            elif user_payment.lower() == "c":
                card_type: str = input("[!] Please write the type of your card: eg. Credit  ")
                key_card = input("[?] Please insert the Key of your card. eg. 0000  ")
                try:
                    key_card = int(key_card)
                    card_1 = Card(card_type, key_card)
                    order.set_payment_method(card_1)
                    if card_1.pay(bill-discounts):
                        print("[*] Payment approved, we wish you come back")
                        break
                    else:
                        print("[!] Payment not approved")
                except ValueError:
                    print("[!] Insert a correct key")
    else:
        print("[!]That 100% off will make us break")


if __name__ == "__main__":
    main()