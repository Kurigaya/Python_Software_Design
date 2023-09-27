#Interfaces
class Interfaces:
    def state(self):
        return self.state
    def setState(self, state):
        self.state = state
    def insertCoin(self):
        pass
    def turnCrank(self):
        pass
    def takegumball(self):
        pass
    def takeCoinBack(self):
        pass
    def refill(self):
        pass


class GumballMachine(Interfaces):
    state = None
    bev = None
    noQuarter = None
    hasCoin = None
    release = None
    soldOut = None

    def __init__(self, ball) -> None:
        super().__init__()
        self.noQuarter = NoQuarterState(self)
        self.hasCoin = HasCoinState(self)
        self.release = ReleaseState(self)
        self.soldOut = SoldOutState(self)
        self.setState(self.noQuarter)
        if ball == 0:
            self.setState(self.soldOut)
        
    def setState(self, state):
        self.state = state
    def insertCoin(self):
        self.state.insertCoin()
    def turnCrank(self):
        self.state.turnCrank()
    def takeGumball(self):
        self.state.takegumball()
    def takeCoinBack(self):
        self.state.takeCoinBack()
    def refill(self, ingred, quan):
        self.state.refill(ingred, quan)

class NoQuarterState(Interfaces):
    def __init__(self, gumballMachine: GumballMachine):
        self.gumballMachine = gumballMachine
    def insertCoin(self):
        self.gumballMachine.setState(self.gumballMachine.hasCoin)
    def turnCrank(self):
        print("Insert quarter first!")
    def takeGumball(self):
        print("Insert quarter first!")
    def takeCoinBack(self):
        print("You didn't insert any coin!")
    def refill(self, ingred, quan):
        print("You cannot refill!")


class HasCoinState(Interfaces):
    def __init__(self, gumballMachine: GumballMachine):
        self.gumballMachine = gumballMachine
    def insertCoin(self):
        print("Thank for tips")
    def turnCrank(self):
        print("Here is your ball.")
        self.gumballMachine.setState(self.gumballMachine.release)
    def takeGumball(self):
        print("...")
    def takeCoinBack(self):
        print("...")
    def refill(self, ingred, quan):
        print("...")

class ReleaseState(Interfaces):
    def __init__(self, gumballMachine: GumballMachine):
        self.gumballMachine = gumballMachine
    def insertCoin(self):
        print("Thank for tips")
    def turnCrank(self):
        print("You have turned crank already.")
    def takeGumball(self):
        print("Thank you!! see you later.")
        self.gumballMachine.setState(self.gumballMachine.noQuarter)
    def takeCoinBack(self):
        print("Only take ball pls.")
    def refill(self, ingred, quan):
        print("No refill at the moment.")

class SoldOutState(Interfaces):
    def __init__(self, gumballMachine: GumballMachine):
        self.gumballMachine = gumballMachine
    def insertCoin(self):
        print("No bev today, pls take your coin back")
    def turnCrank(self):
        print("No bev today.")
    def takeGumball(self):
        print("No bev today.")
    def takeCoinBack(self):
        print("No bev today.")
    def refill(self, ingred, quan):
        self.refillIngred(ingred, quan)

def main():
    gumballMachine = GumballMachine(1)
    gumballMachine.insertCoin()
    gumballMachine.turnCrank()
    gumballMachine.takeGumball()


    gumballMachine2 = GumballMachine(0)
    gumballMachine2.insertCoin()

main()