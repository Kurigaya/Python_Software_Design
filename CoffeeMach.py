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

class WaitForOrder(State):
    def __init__(self, coffeeMachine: CoffeeMachine):
        self.coffeeMachine = coffeeMachine
        print("Hello, which coffee you looking for :)")
    def selectMenu(self):
        print("Menu:")
        print("Cappuccino >>  Dark Roast 20g, Steamed Milk 200 cc")
        print("Late >>  House Blend 20g, Soy Milk 200 cc")
        print("Mocha Late >>  House Blend 20g, Soy Milk 200 cc, Chocolate 50 cc")
        while True:
            beverage = input("Enter your coffee: ")
            match beverage:
                case "Cappuccino":
                    self.coffeeMachine.bev = Milk(DarkRoast())
                    self.coffeeMachine.takeIngred("Milk", 200)
                    self.coffeeMachine.takeIngred("DarkRoast", 20)
                    break
                case "Late":
                    self.coffeeMachine.bev = SoyMilk(HouseBlend())
                    self.coffeeMachine.takeIngred("SoyMilk", 200)
                    self.coffeeMachine.takeIngred("HouseBlend",20)
                    break
                case "Mocha Late":
                    self.coffeeMachine.bev = Chocolate(SoyMilk(HouseBlend()))
                    self.coffeeMachine.takeIngred("Chocolate", 50)
                    self.coffeeMachine.takeIngred("SoyMilk", 200)
                    self.coffeeMachine.takeIngred("HouseBlend", 20)
                    break
                case _ :
                    continue
        print(f"Your menu is {beverage}")

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

#Interfaces for Coffee Decorator
class CoffeeComponent():
    def __init__(self) -> None:
        pass
    def coffeeName(self):
        pass
    def cost(self):
        pass

class HouseBlend(CoffeeComponent):
    def __init__(self):
        self.coffee = "HouseBlend"

    def coffeeName(self):
        return self.coffee

    def cost(self):
        return 0.89

class DarkRoast(CoffeeComponent):
    def __init__(self):
        self.coffee = "DarkRoast"
    
    def coffeeName(self):
        return self.coffee
    
    def cost(self):
        return 0.99

#Decorator
class Milk(CoffeeComponent):
    def __init__(self, coffee):
        self.coffee = coffee
    
    def coffeeName(self):
        return self.coffee.coffeeName() + " + Milk"
    
    def cost(self):
        return self.coffee.cost() + 0.10

class Mocha(CoffeeComponent):
    def __init__(self, coffee):
        self.coffee = coffee
    def coffeeName(self):
        return self.coffee.coffeeName() + " + Mocha"
    def cost(self):
        return self.coffee.cost() + 0.20
    
class SoyMilk(CoffeeComponent):
    def __init__(self, coffee):
        self.coffee = coffee
    def cost(self):
        return self.coffee.cost() + 0.15
    def coffeeName(self):
        return self.coffee.coffeeName() + " + SoyMilk"

class Whip(CoffeeComponent):
    def __init__(self, coffee):
        self.coffee = coffee
    def cost(self):
        return self.coffee.cost() + 0.10
    def coffeeName(self):
        return self.coffee.coffeeName() + " + Whip"

class Chocolate(CoffeeComponent):
    def __init__(self, coffee):
        self.coffee = coffee
    def cost(self):
        return self.coffee.cost() + 0.20
    def coffeeName(self):
        return self.coffee.coffeeName() + " + Chocolate"
    
def main():
    coffee_machine = CoffeeMachine()
    coffee_machine.selectMenu()
    coffee_machine.confirmMenu()
    coffee_machine.insertCoin()
    coffee_machine.turnCrank()
    coffee_machine.takeCoffee()


main()
