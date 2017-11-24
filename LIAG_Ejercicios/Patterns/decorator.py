from functools import wraps
"""dynamically add functionality to an Object.
Name:Leonardo Israel Aguayo González"""

def make_blink(function):
    """Definition the decorator"""
    @wraps(function)

    def decorator():
        ret= function()
        return "<blink>"+ ret+ "</blink>"
    return decorator
#Apply the decorator here!
@make_blink
def hello_word():
    """Original function"""

    return "Hello, world! "

#chech the result of decorating
print(hello_word())

#check if the function name is still the same name of the function bering decorate
print(hello_word,__name__)
#check if the docstring is still the same as that of the function being decorated
print(hello_word, __doc__)