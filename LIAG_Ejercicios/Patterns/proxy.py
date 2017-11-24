import time
"""provides an intermediary for an object to control its access..
Name: Leonardo Israel Aguayo González"""
class Producer:

    def producer(self):
        print("Producer has time to meet you know!")

class Proxy:

    def __init__(self):
        self.occupied='No'
        self.producer= None

    def producer(self):
        print("Artist checking if Producer is available ...")

        if self.occupied=='No':
            self.producer=Producer()
            time.sleep(2)

            self.producer.meet()

        else:
            time.sleep(2)
            print("Producer is busy!")

p=Proxy()

#Make the proxy : Artist produce until Producer is available
p=Producer()

#Change the state to occupied
p.occupied='Yes'

#Make the Producer producer
p.producer()