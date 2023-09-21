from abc import ABC, abstractclassmethod

#Beverage Interfaces
class Beverage(ABC):
    def bevName(self):
        pass
    def cost(self):
        pass
    def getIngred(self):
        pass

#Decorator
class Milk(Beverage):
    def __init__(self, bev):
        self.bev = bev
        self.ingred = {"Milk":200}
    def bevName(self):
        return self.bev.bevName() + " + Milk"
    def cost(self):
        return self.bev.cost() + 0.10
    def getIngred(self):
        ingredients = self.bev.getIngred().copy()  # Copy the base ingredients
        ingredients.update(self.ingred) 
        return ingredients
class SoyMilk(Beverage):
    def __init__(self, bev):
        self.bev = bev
        self.ingred = {"SoyMilk":20}
    def cost(self):
        return self.bev.cost() + 0.15
    def bevName(self):
        return self.bev.bevName() + " + SoyMilk"
    def getIngred(self):
        ingredients = self.bev.getIngred().copy()  # Copy the base ingredients
        ingredients.update(self.ingred)
        return ingredients
class Whip(Beverage):
    def __init__(self, bev):
        self.bev = bev
        self.ingred = {"Whip":100}
    def cost(self):
        return self.bev.cost() + 0.10
    def bevName(self):
        return self.bev.bevName() + " + Whip"
    def getIngred(self):
        ingredients = self.bev.getIngred().copy()  # Copy the base ingredients
        ingredients.update(self.ingred) 
        return ingredients
class Chocolate(Beverage):
    def __init__(self, bev):
        self.bev = bev
        self.ingred = {"Chocolate":50}
    def cost(self):
        return self.bev.cost() + 0.20
    def bevName(self):
        return self.bev.bevName() + " + Chocolate"
    def getIngred(self):
        ingredients = self.bev.getIngred().copy()  # Copy the base ingredients
        ingredients.update(self.ingred) 
        return ingredients
class Lemon(Beverage):
    def __init__(self, bev):
        self.bev = bev
        self.ingred = {"Lemon": 30}
    def cost(self):
        return self.bev.cost() + 0.50
    def bevName(self):
        return self.bev.bevName() + " + Lemon"
    def getIngred(self):
        ingredients = self.bev.getIngred().copy()  # Copy the base ingredients
        ingredients.update(self.ingred) 
        return ingredients
class Iced(Beverage):
    def __init__(self, bev):
        self.bev = bev
        self.ingred = {"Iced": 30}
    def cost(self):
        return self.bev.cost() + 0.20
    def bevName(self):
        return self.bev.bevName() + " + Iced"
    def getIngred(self):
        ingredients = self.bev.getIngred().copy()  # Copy the base ingredients
        ingredients.update(self.ingred) 
        return ingredients
    
#Concrete Beverage menu
    #Coffee menu
class DarkRoast(Beverage):
    def __init__(self):
        self.bev = "DarkRoast"
        self.ingred = {"DarkRoast":20}
    def bevName(self):
        return self.bev
    def cost(self):
        return 0.99
    def getIngred(self):
        return self.ingred
class HouseBlend(Beverage):
    def __init__(self) :
        self.bev = "HouseBlend"
        self.ingred = {"HouseBlend":20}
    def bevName(self):
        return self.bev
    def cost(self):
        return 0.89
    def getIngred(self):
        return self.ingred
class Base_Coffee(Beverage):
    def __init__(self):
        self.bev = "Coffee"
        self.ingred = {"Coffee": 20}
    def bevName(self):
        return self.bev
    def cost(self):
        return 0.60
    def getIngred(self):
        return self.ingred
    #Tea menu
class BlackTea(Beverage):
    def __init__(self):
        self.bev = "Black Tea"
        self.ingred = {"BlackTea":20}
    def bevName(self):
        return self.bev
    def cost(self):
        return 0.50
    def getIngred(self):
        return self.ingred
class WhiteTea(Beverage):
    def __init__(self):
        self.bev = "White Tea"
        self.ingred = {"WhiteTea":20}
    def bevName(self):
        return self.bev
    def cost(self):
        return 0.70
    def getIngred(self):
        return self.ingred
class GreenTea(Beverage):
    def __init__(self):
        self.bev = "Green Tea"
        self.ingred = {"GreenTea":20}
    def bevName(self):
        return self.bev
    def cost(self):
        return 0.70
    def getIngred(self):
        return self.ingred


#Interfaces Menu
class IMenu():
    def bevName(self):
        return self.bev.bevName()
    def cost(self):
        return self.bev.cost()
    def getIngred(self):
        return self.bev.getIngred()
#Coffee Menu
class Cuppuccino(IMenu):
    def __init__(self):
        self.bev = Milk(DarkRoast())
class Late(IMenu):
    def __init__(self):
        self.bev = Milk(DarkRoast())
class MochaLate(IMenu):
    def __init__(self):
        self.bev = Milk(DarkRoast())
#Tea Menu
class LemonTea(IMenu):
    def __init__(self):
        self.bev = Lemon(GreenTea())
class MilkTea(IMenu):
    def __init__(self):
        self.bev = Milk(GreenTea())
class IcedGreenTea(IMenu):
    def __init__(self):
        self.bev = Iced(GreenTea())

#Abstract Factory
class IBevFactory(ABC):
    @abstractclassmethod
    def brew(self):
        pass
#Creator Interfaces
class CoffeeFactory(IBevFactory):
    def brew(self, bev):
        if bev == "Cuppuccino":
            return Cuppuccino()
        elif bev == "Late":
            return Late()
        elif bev == "Mocha Late":
            return MochaLate()
        elif bev == "Custom coffee":
            print("Begin with Normal Coffee.")
            print("1.Milk\n2.Iced\n3.Chocolate\n4.SoyMilk\n5.Whip")
            while True:
                dec = input("Which add-on you prefer (1/2/3/4/5/ 6 for No)")
                decs = {
                    '1': Milk(),
                    '2': Iced(),
                    '3': Chocolate(),
                    '4': SoyMilk(),
                    '5': Whip()
                }
                if dec in decs:
                    decorator = decs[dec]
                    return decorator(Base_Coffee())
                elif dec == "6":
                    return Base_Coffee()
        return False
class TeaFactory(IBevFactory):
    def brew(self, bev):
        if bev == "Iced Green Tea":
            return IcedGreenTea()
        elif bev == "Milk Tea":
            return MilkTea()
        elif bev == "Lemon Tea":
            return LemonTea()
        elif bev == "Custom tea":
            print("Tea:")
            print("1.Green Tea\n2.White Tea\n3.Black Tea")
            while True:
                tea = input("Which tea you prefer (1/2/3): ")
                teas = {
                    '1': GreenTea(),
                    '2': WhiteTea(),
                    '3': BlackTea()
                }
                if tea in teas:
                    break
            print("Want to decorate some of these?")
            print("1.Milk\n2.Iced\n3.Lemon")
            while True:
                dec = input("Which add-on you prefer (1/2/3/ 4 for No)")
                decs = {
                    '1': Milk(),
                    '2': Iced(),
                    '3': Lemon()
                }
                if dec in decs:
                    decorator = decs[dec]
                    return decorator(teas[tea])
                elif dec == "4":
                    return teas[tea]
        return False

#Interfaces for Beverage Machine
class State(ABC):
    def __init__(self) -> None:
        pass
    def setState(self, state):
        self.state = state
    def selectMenu(self)-> None:
        pass
    def confirmMenu(self)-> None:
        pass
    def insertCoin(self)-> None:
        pass
    def turnCrank(self)-> None:
        pass
    def takeCoffee(self)-> None:
        pass
    def takeCoinBack(self)-> None:
        pass
    def refill(self)-> None:
        pass

class Inventory:
    def __init__(self) -> None:
        self.Ingredients = {"Chocolate": 500,
                            "Milk": 500,
                            "SoyMilk": 500,
                            "DarkRoast": 100,
                            "HouseBlend": 100,
                            "GreenTea": 100,
                            "BlackTea": 100,
                            "WhiteTea": 100,
                            "Lemon": 200,
                            "Iced": 500
                            }

    def enoughIngred(self, ingreds):
        for ingred in ingreds:
            quan = ingreds[ingred]
            if ingred in self.Ingredients and self.Ingredients[ingred] >= quan:
                pass
            else:
                return False
        return True
    def takeIngreds(self, ingreds):
        for ingred in ingreds:
            quan = ingreds[ingred]
            self.Ingredients[ingred] -= quan
    def refillIngred(self, ingred, quan):
        self.Ingredients[ingred] += quan
    def checkIngred(self):
        print(f"Inventory reamining : {self.Ingredients}")

class CoffeeMachine(Inventory, State):
    state = None
    bev = None
    waitForOrder = None
    hasCoin = None
    release = None
    soldOut = None

    def __init__(self) -> None:
        super().__init__()
        self.waitForOrder = WaitForOrder(self)
        self.hasCoin = HasCoin(self)
        self.release = ReleaseCoffee(self)
        self.soldOut = SoldOut(self)
        self.setState(self.waitForOrder)
        
    def setState(self, state):
        self.state = state
    def selectMenu(self):
        self.state.selectMenu()
    def confirmMenu(self):
        self.state.confirmMenu()
    def insertCoin(self):
        self.state.insertCoin()
    def turnCrank(self):
        self.state.turnCrank()
    def takeCoffee(self):
        self.state.takeCoffee()
    def takeCoinBack(self):
        self.state.takeCoinBack()
    def refill(self, ingred, quan):
        self.state.refill(ingred, quan)

class WaitForOrder(State):
    def __init__(self, coffeeMachine: CoffeeMachine):
        self.coffeeMachine = coffeeMachine
    def selectMenu(self):
        bev = input("Coffee or Tea (1/2): ")
        if bev == "1":
            print("Menu:\n1. Cuppuccino\n2. Late\n3. Mocha Late\n4. Custom coffee")
            while True:
                beverage = input("Enter your bev (1/2/3/4): ")
                menus = {
                    '1': "Cuppuccino",
                    '2': "Late",
                    '3': "Mocha Late",
                    '4': "Custom coffee"
                }
                factory = CoffeeFactory()
                if beverage in menus:
                    self.coffeeMachine.bev = factory.brew(menus[beverage])
                    self.coffeeMachine.takeIngreds(self.coffeeMachine.bev.getIngred())
                    print(f"You selected: {self.coffeeMachine.bev.bevName()}")
                    print(f"It needed {self.coffeeMachine.bev.getIngred()}")
                    break
                else:
                    print("Invalid choice!")
        elif bev == "2":
            print("Menu:\n1. Iced Green Tea\n2. Milk Tea\n3. Lemon Tea\n4. Custom tea")
            while True:
                beverage = input("Enter your bev (1/2/3/4): ")
                menus = {
                    '1': "Iced Green Tea",
                    '2': "Milk Tea",
                    '3': "Lemon Tea",
                    '4': "Custom tea"
                }
                factory = TeaFactory()
                if beverage in menus:
                    self.coffeeMachine.bev = factory.brew(menus[beverage])
                    self.coffeeMachine.takeIngreds(self.coffeeMachine.bev.getIngred())
                    print(f"You selected: {self.coffeeMachine.bev.bevName()}")
                    print(f"It needed {self.coffeeMachine.bev.getIngred()}")
                    break
                else:
                    print("Invalid choice!")

    def confirmMenu(self):
        print(f"Insert coin for {self.coffeeMachine.bev.cost()}")
    def insertCoin(self):
        self.coffeeMachine.setState(self.coffeeMachine.hasCoin)
    def turnCrank(self):
        print("Confirm your order first!")
    def takeCoffee(self):
        print("Confirm your order first!")
    def takeCoinBack(self):
        print("You didn't insert any coin!")
    def refill(self, ingred, quan):
        print("You cannot refill!")


class HasCoin(State):
    def __init__(self, coffeeMachine: CoffeeMachine):
        self.coffeeMachine = coffeeMachine
    def selectMenu(self):
        print("You need more bev?")
    def confirmMenu(self):
        print("You have confirmed this menu already!")
    def insertCoin(self):
        print("Thank for tips")
    def turnCrank(self):
        print("Wait for your bev, we are brewing...")
        print("Finished!!! Here is your bev.")
        self.coffeeMachine.setState(self.coffeeMachine.release)
    def takeCoffee(self):
        print("...")
    def takeCoinBack(self):
        print("...")
    def refill(self, ingred, quan):
        print("...")

class ReleaseCoffee(State):
    def __init__(self, coffeeMachine: CoffeeMachine):
        self.coffeeMachine = coffeeMachine
    def selectMenu(self):
        print("Take your bev first.")
    def confirmMenu(self):
        print("You have confirm already, pls take your bev.")
    def insertCoin(self):
        print("Thank for tips")
    def turnCrank(self):
        print("You have turned crank already.")
    def takeCoffee(self):
        print("Thank you!! see you later.")
        self.coffeeMachine.setState(self.coffeeMachine.waitForOrder)
    def takeCoinBack(self):
        print("Only take bev pls.")
    def refill(self, ingred, quan):
        print("No refill at the moment.")

class SoldOut(State):
    def __init__(self, coffeeMachine: CoffeeMachine):
        self.coffeeMachine = coffeeMachine
    def selectMenu(self):
        print("No bev today.")
    def confirmMenu(self):
        print("No bev today.")
    def insertCoin(self):
        print("No bev today.")
    def turnCrank(self):
        print("No bev today.")
    def takeCoffee(self):
        print("No bev today.")
    def takeCoinBack(self):
        print("No bev today.")
    def refill(self, ingred, quan):
        self.refillIngred(ingred, quan)

class BangkokCoffeeMachine(CoffeeMachine):
    def __init__(self, current) -> None:
        super().__init__()
        self.waitForOrder = WaitForOrder(self)
        self.hasCoin = HasCoin(self)
        self.release = ReleaseCoffee(self)
        self.soldOut = SoldOut(self)
        if current != 0:
            self.setState(self.waitForOrder)
        else:
            self.setState(self.soldOut)

class NakornCoffeeMachine(CoffeeMachine):
    def __init__(self, current) -> None:
        super().__init__()
        self.waitForOrder = WaitForOrder(self)
        self.hasCoin = HasCoin(self)
        self.release = ReleaseCoffee(self)
        self.soldOut = SoldOut(self)
        if current != 0:
            self.setState(self.waitForOrder)
        else:
            self.setState(self.soldOut)

def main():
    #Correct client behavior
    coffeeMachine = BangkokCoffeeMachine(1) #parameter can be any except 0 for init bev machine
    coffeeMachine.selectMenu()
    coffeeMachine.confirmMenu()
    coffeeMachine.insertCoin()
    coffeeMachine.turnCrank()
    coffeeMachine.takeCoffee()
    coffeeMachine.checkIngred()
    print("*"*30)
    #Sold Out State
    coffeeMachine2 = NakornCoffeeMachine(0) #Set state to SoldOut state
    coffeeMachine2.selectMenu()
    print("*"*30)
    coffeeMachine3 = NakornCoffeeMachine(1)
    coffeeMachine3.selectMenu()


main()

