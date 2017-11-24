"""is used to transform an interface into another.
Name:Leonardo Israel Aguayo González"""
class Korean:
    """Korean speaker"""

    def __init__(self):
        self.name = "Korean"

    def speak_korean(self):
        return "An-meyong?"


class British:
    """English speaker"""

    def __init__(self):
        self.name = "British"

    def speak_english(self):
        return "Hello!"


class Adapter:
    """This change the generic method name to individual method names"""
    def __init__(self, object, **adapted_method):
        """Chaneg the name of the metod"""
        self._object = object

        self.__dict__.update(adapted_method)

    def __getattr__(self, attr):
        """Simply return the rest of attrubtes!"""
        return getattr(self._object, attr)


# List to store speaker object
objects = []

# Create a Korean Object
korean = Korean()
# Create a British object
british = British()

# Append the object to the objetct list
objects.append(Adapter(korean, speak=korean.speak_korean()))
objects.append(Adapter(british, speak=british.speak_english()))

for obj in objects:
    print("{} says '{}' \n".format(obj.name, obj.speak()))
