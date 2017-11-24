"""defines a dependency of type one to many between objects,so that when one of the objects changes its state,it notifies this change to all dependents
Name:Leonardo Israel Aguayo González"""

class Subject(object): #Represents what is being 'observed'
    def __init__(self):
        self._observers = [] # This where references to all the observers are being kept
                             # Note that this is a one-to-many relationship: there will
                             # be one subject to be observed by multiple_observers
    def attach(self, observer):
        if observer not in self._observers: #If the observer is not already in the observers list
            self._observers.append(observer)
        # append the observer to the list

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier=None):
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)
        #For all the observers in the list
            #Don't notify the observer who is actually updating the temperature
                #Alert the observers!

class Core(Subject):

    def __init__(self, name:""):
        Subject.__init__(self)
        self._name = name
        self._temp = 0
    @property #Getter that gets the core temperature
    def temp(self):
        return self._temp

    @temp.setter #Setter that sets the core temperature
    def temp(self, temp):
        self._temp = temp

class TempViewer:

    def update(self, subject): #Alert method that is invoked when the notify() in a concrete is invoked
        print("Temperature Viewer: {} has Temperature {}".format(subject._name, subject._temp))


#let´s create our subjects
c1 = Core("Core 1")
c2 = Core("Core 2")

#let's create our observers
v1 = TempViewer()
v2 = TempViewer()

#let´s attach our observers
c1.attach(v1)
c1.attach(v1)

#change the temperature
c1.temp = 80
c1.temp = 90


