############################################################################
# Create a Pets class that holds instances of dogs; 
# this class is completely separate from the Dog class. 
# In other words, the Dog class does not inherit from the Pets class. 
# Then assign three dog instances to an instance of the Pets class
# Your output should look like
# I have 3 dogs.
# Tom is 6.
# Fletcher is 7.
# Larry is 9. 
#############################################################################

class Pets:
    def __init__(self, host):
        self._host = host
        self._dogs = []

    def addDog(self, dog):
        self._dogs.append(dog)

    def getDogs(self):
        return self._dogs

    def getDogInfo(self, dog):
        return dog

    def getHost(self):
        return self._host

    def __str__(self):
        return f"{self._host} have {len(self._dogs)} dogs."

class Dog:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def __str__(self):
        return f"{self._name} is {self._age}."

tom = Dog("Tom", 6)
fletcher = Dog("Fletcher", 7)
larry = Dog("Larry", 9)
i = Pets("I")
i.addDog(tom)
i.addDog(fletcher)
i.addDog(larry)
if len(i.getDogs()):
    print(i)
    for each in i.getDogs():
        print(each)
else:
    print(f"{i.getHost()} have no dogs.")