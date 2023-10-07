class Parent:
    def __init__(self,greet,thing):
        self.__greet = greet# You have to encapsulate by writing --(BUT IN DOWN!)NOW IT IS UNCHANGABLE AND NON PUBLIC
        self.thing = thing
        print(self.__greet)
a = Parent("hello","world")
# print(a.greet,a.thing)# THAT WILL RAISE AN ERROR FOR SOLUTION LOOK AT LINE 5
print(a.thing)