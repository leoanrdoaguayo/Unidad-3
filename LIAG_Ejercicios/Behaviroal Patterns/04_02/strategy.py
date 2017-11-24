import types #Import the types module

"""It is determined how messages should be exchanged between different objects to solve a task
Name:Leonardo Israel Aguayo González"""

class Strategy:
    """The Strategy Pattern class"""
    def __init__(self, fuction=None):
        self.name = "Default Strategy"


    def execute(self):
        """The default method that prints the name of the strategy being used"""
        print("{} is used!".format(self.name))

#Replacement method 1
def strategy_one(self):
    print("{} is used to execute method 1".format(self.name))

def strategy_two(self):
    print("{} is used to execute method 2".format(self.name))

s0 = Strategy()
s0.execute()

s1 = Strategy(strategy_one)
s1.name ="Strategy one"
s1.execute()

s2 = Strategy(strategy_two)
s2.name="Strategy two"
s2.execute()

