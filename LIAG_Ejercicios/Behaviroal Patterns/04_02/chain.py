"""allows establishing a chain of receiving objects through which a request made by a sending object is passed.
Name:Leonardo Israel Aguayo González"""

class Handler: #Abstract Handler
    """Abstract Handler"""
    def __init__(self, successor):
        self._successor = successor

    def handle(self, request):
        handled = self._handle(request)

        if not handled:
            self._successor.handle(request)

    def _handle(self, request):
        raise NotImplementedError("Must provide implementation in subclass!")

class ConcreteHandler1(Handler):
    """Concrete handler 1"""
    def _handle(self, request):
        if 0 < request <= 10:
            print("Request {} handled in handler 1".format(request))
            return True

class DefaultHandler(Handler):
    """Dafault handler"""
    def _handle(self, request):
        print("End of chain, no handler for {}".format(request))
        return True
class Client:
    def __init__(self):
        self.handler = ConcreteHandler1(DefaultHandler(None))

    def delegate(self, requests):
        for request in requests:
            self.handler.handle(request)

#create a client
c = Client()
#Create requests
requests = [2, 5, 30]
#Send the request
c.delegate(requests)
