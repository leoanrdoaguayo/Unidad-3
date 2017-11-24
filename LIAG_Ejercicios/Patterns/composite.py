"""it serves to construct complex objects from other simpler and similar ones between
Name:Leonardo Israle Aguayo González"""
class Component(object):
    """Abstrac class"""

    def __init__(self, *args,**kwargs):
        pass

    def component_function(self):
        pass

class Child(Component):
    """Concrete class"""

    def __init__(self,*args,**kwargs):
        Component.__init__(self,*args,**kwargs)

        self.name=args[0]

    def component_function(self):
        print("{} ".format(self.name))

class Composite(Component):
    def __init__(self,*args,**kwargs):
        Component.__init__(self,*args,**kwargs)
        #This is where we store the name of the compiste object
        self.name=args[0]
        #this is where we keep our child items
        self.children=[]
    def append_child(self,child):
        self.children.append(child)

    def remove_child(self,child):
        self.children.remove(child)

    def component_function(self):
        print("{}".format(self.name))

        for i in self.children:
            i.component_function()

#Build a composite submenu
sub1=Composite("Submenu1")

#Create a new child sub_submenu 11
sub11=Child("sub_submenu 11")
#Create a new child sub_submenu 12
sub12=Child("sub_submenu 12")

#Add the submenu 11 to submenu 1
sub1.append_child(sub11)
#Add the submenu 12 to submenu 1
sub1.append_child(sub12)
#Build a top level composite menu
top=Composite("top_menu")
#Build a submenu 2 that is not a composite menu
sub2=Child("submenu2")

top.append_child(sub1)
top.append_child(sub2)
