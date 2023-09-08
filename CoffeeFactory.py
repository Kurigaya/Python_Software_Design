from abc import ABC, abstractclassmethod

#Coffee Interfaces
class Coffee(ABC):
    def brewCoffee(self):
        pass
    def coffeeName(self):
        pass
    def cost(self):
        pass

#Concrete Coffee menu
class DarkRoast(Coffee):
    def brewCoffee(self):
        return "DarkRoast"
    def cost(self):
        return 0.99
    
class HouseBleand(Coffee):
    def __init__(self) -> None:
        self.coffee = "HouseBlend"
    def brewCoffee(self):
        self.coffee = "HouseBlend"
    def coffeeName(self):
        return self.coffee
    def cost(self):
        return 0.89
    
#Creator Interfaces
class CoffeeFactory(ABC):
    def brewCoffee(self):
        pass

#Concrete Creators
class DarkRoastFactory(CoffeeFactory):
    def brewCoffee(self):
        return DarkRoast()
    def getCoffee(self):
        pass
    
    
class HouseBlendFactory(CoffeeFactory):
    def brewCoffee(self):
        return HouseBleand()
    
def main():
    coffeeFactory = DarkRoastFactory().brewCoffee()
    print(f"Your coffee is {coffeeFactory.brewCoffee()} at ${coffeeFactory.cost()}")
    coffeeFactory2 = HouseBlendFactory().brewCoffee()
    print(f"Second coffee is {coffeeFactory2.coffeeName()}")

main()