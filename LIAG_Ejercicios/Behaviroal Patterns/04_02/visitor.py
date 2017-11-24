"""will separate the algorithm from the structure of an object.
Name: Leonardo Israel Aguayo González."""

class House(object):
    def accept(self, visitor):
        """Interface to accept the visitor"""
        visitor.visit(self)

    def work_on_hvac(self, hvac_specialist):
        print("worked on by: ", hvac_specialist) #Note that we now have a reference to the HVAC specialist object in the house object

    def work_on_electricity(self, electrician):
        print("worked on by: ", electrician)

    def __str__(self):
        return self.__class__.__name__

class Visitor(object):
    def __str__(self):
        return self.__class__.__name__

class HvacSpecialist(Visitor):
    def visit(self, house):
        house.work_on_hvac(self)

class Electrician(Visitor):
    def visit(self, house):
        house.work_on_electricity(self)


#Create a HVAC specialist
hv = HvacSpecialist()
#Create an electrician
e = Electrician()
#Create a house
home = House()
#let the house accept the HVAC specialst and work on the house by invoking visit() method
home.accept(hv)
#let the hoouse accept the electrician and work on the house by invoking visit() method
home.accept(e)