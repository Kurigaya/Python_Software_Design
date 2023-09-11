from abc import ABC, abstractclassmethod

#Coffee Interfaces
class Coffee(ABC):
    def brewCoffee(self):
        pass
    def coffeeName(self):
        pass
    def cost(self):
        pass
    def ingred(self):
        pass

#Decorator
class Milk(Coffee):
    def __init__(self, coffee):
        self.coffee = coffee
        self.ingred = {"Milk":200}
    def coffeeName(self):
        return self.coffee.coffeeName() + " + Milk"
    def cost(self):
        return self.coffee.cost() + 0.10
    def getIngred(self):
        ingredients = self.coffee.getIngred().copy()  # Copy the base ingredients
        ingredients.update(self.ingred)  # Update with Milk ingredient
        return ingredients
    
class SoyMilk(Coffee):
    def __init__(self, coffee):
        self.coffee = coffee
        self.ingred = {"SoyMilk":20}
    def cost(self):
        return self.coffee.cost() + 0.15
    def coffeeName(self):
        return self.coffee.coffeeName() + " + SoyMilk"
    def getIngred(self):
        ingredients = self.coffee.getIngred().copy()  # Copy the base ingredients
        ingredients.update(self.ingred)  # Update with Milk ingredient
        return ingredients

class Whip(Coffee):
    def __init__(self, coffee):
        self.coffee = coffee
        self.ingred = {"Whip":100}
    def cost(self):
        return self.coffee.cost() + 0.10
    def coffeeName(self):
        return self.coffee.coffeeName() + " + Whip"
    def getIngred(self):
        ingredients = self.coffee.getIngred().copy()  # Copy the base ingredients
        ingredients.update(self.ingred)  # Update with Milk ingredient
        return ingredients
class Chocolate(Coffee):
    def __init__(self, coffee):
        self.coffee = coffee
        self.ingred = {"Chocolate":50}
    def cost(self):
        return self.coffee.cost() + 0.20
    def coffeeName(self):
        return self.coffee.coffeeName() + " + Chocolate"
    def getIngred(self):
        ingredients = self.coffee.getIngred().copy()  # Copy the base ingredients
        ingredients.update(self.ingred)  # Update with Milk ingredient
        return ingredients
#Concrete Coffee menu
class DarkRoast(Coffee):
    def __init__(self) -> None:
        self.coffee = "DarkRoast"
        self.ingred = {"DarkRoast":20}
    def coffeeName(self):
        return self.coffee
    def cost(self):
        return 0.99
    def getIngred(self):
        return self.ingred
    
class HouseBlend(Coffee):
    def __init__(self) -> None:
        self.coffee = "HouseBlend"
        self.ingred = {"HouseBlend":20}
    def coffeeName(self):
        return self.coffee
    def cost(self):
        return 0.89
    def ingred(self):
        return self.ingred

#Menu
class Cuppuccino(Coffee):
    def __init__(self):
        self.coffee = "Cuppuccino"
        self.bev = Milk(DarkRoast())
    def coffeeName(self):
        return self.coffee
    def cost(self):
        return self.bev.cost()
    def getIngred(self):
        return self.bev.getIngred()

class Late(Coffee):
    def __init__(self):
        self.coffee = "Late"
        self.bev = Milk(DarkRoast())
    def coffeeName(self):
        return self.coffee
    def cost(self):
        return self.coffee.cost()
    def getIngred(self):
        return self.bev.getIngred()

    
class MochaLate(Coffee):
    def __init__(self):
        self.coffee = "Mocha Late"
        self.bev = Milk(DarkRoast())
    def coffeeName(self):
        return self.coffee
    def cost(self):
        return self.coffee.cost()
    def getIngred(self):
        return self.bev.getIngred()

#Creator Interfaces
class CoffeeFactory(ABC):
    def brewCoffee(self):
        pass

#Concrete Creators
class CuppuccinoFactory(CoffeeFactory):
    def brewCoffee(self):
        return Cuppuccino()
class LateFactory(CoffeeFactory):
    def brewCoffee(self):
        return Late()
class MochaLateFactory(CoffeeFactory):
    def brewCoffee(self):
        return MochaLate()

#Interfaces for Coffee Machine
class State():
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
        self.Ingredients = {"Chocolate": 5000,
                            "Milk": 5000,
                            "SoyMilk": 5000,
                            "DarkRoast": 1000,
                            "HouseBlend": 1000}
    
    def takeIngred(self, ingred, quan):
        if ingred in self.Ingredients and self.Ingredients[ingred] >= quan:
            self.Ingredients[ingred] -= quan
        else:
            print(f"Not enough {ingred}")
    def refillIngred(self, ingred, quan):
        self.Ingredients[ingred] += quan
    def checkIngred(self):
        print(f"Inventory reamining : {self.Ingredients}")

class CoffeeMachine(Inventory):
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
    def confirmMenu(self)-> None:
        self.state.confirmMenu()
    def insertCoin(self):
        self.state.insertCoin()
    def turnCrank(self):
        self.state.turnCrank()
    def takeCoffee(self):
        self.state.takeCoffee()
    def takeCoinBack(self):
        self.state.takeCoinBack()
    def refill(self):
        self.state.refill()
    def takeIngreds(self, ingreds):
        for ingred in ingreds:
            quan = ingreds[ingred]
            self.takeIngred(ingred, quan)

class WaitForOrder(State):
    def __init__(self, coffeeMachine: CoffeeMachine):
        self.coffeeMachine = coffeeMachine
        print("Hello, which coffee you looking for :)")
    def selectMenu(self):
        print("Menu:")
        print("1. Cuppuccino")
        print("2. Late")
        print("3. Mocha Late")
        while True:
            beverage = input("Enter your coffee (1/2/3): ")
            factories = {
            '1': CuppuccinoFactory(),
            '2': LateFactory(),
            '3': MochaLateFactory(),  # Assuming Mocha Late uses DarkRoast as a base
            }

            if beverage in factories:
                factory = factories[beverage]
                self.coffeeMachine.bev = factory.brewCoffee()
                self.coffeeMachine.takeIngreds(self.coffeeMachine.bev.getIngred())
                print(f"You selected: {self.coffeeMachine.bev.coffeeName()}")
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
    def refill(self):
        print("You cannot refill!")


class HasCoin(State):
    def __init__(self, coffeeMachine: CoffeeMachine):
        self.coffeeMachine = coffeeMachine
    def selectMenu(self):
        print("You need more coffee?")
    def confirmMenu(self):
        print("You have confirmed this menu already!")
    def insertCoin(self):
        print("Thank for tips")
    def turnCrank(self):
        print("Wait for your coffee, we are brewing...")
        print("Finished!!! Here is your coffee.")
        self.coffeeMachine.setState(self.coffeeMachine.release)
    def takeCoffee(self):
        print("...")
    def takeCoinBack(self):
        print("...")
    def refill(self):
        print("...")

class ReleaseCoffee(State):
    def __init__(self, coffeeMachine: CoffeeMachine):
        self.coffeeMachine = coffeeMachine
    def selectMenu(self):
        print("Wait for finish your coffee first.")
    def confirmMenu(self):
        print("You have confirm already, pls wait.")
    def insertCoin(self):
        print("Thank for tips")
    def turnCrank(self):
        print("Wait")
    def takeCoffee(self):
        print("Thank you!! see you later.")
        self.coffeeMachine.setState(self.coffeeMachine.waitForOrder)
    def takeCoinBack(self):
        print("Only take coffee pls.")
    def refill(self):
        print("No refill at the moment.")

class SoldOut(State):
    def __init__(self, coffeeMachine: CoffeeMachine):
        self.coffeeMachine = coffeeMachine
    def selectMenu(self):
        print("No coffee today.")
    def confirmMenu(self):
        print("No coffee today.")
    def insertCoin(self):
        print("No coffee today.")
    def turnCrank(self):
        print("No coffee today.")
    def takeCoffee(self):
        print("No coffee today.")
    def takeCoinBack(self):
        print("No coffee today.")
    def refill(self, ingred, quan):
        self.refill(ingred, quan)
def main():
    coffeeMachine = CoffeeMachine()
    coffeeMachine.selectMenu()
    coffeeMachine.checkIngred()
    coffeeMachine.selectMenu()
    coffeeMachine.checkIngred()
    # coffeeFactory = CuppuccinoFactory().brewCoffee()
    # print(f"Your coffee is {coffeeFactory.coffeeName()} at ${coffeeFactory.cost()}")
    # coffeeFactory2 = LateFactory().brewCoffee()
    # print(f"Second coffee is {coffeeFactory2.coffeeName()}")

main()