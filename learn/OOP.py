# Class&Objects
class it:
    a = ""
    b = ""

c = it()
d = it()
e = it()

c.a = "data"
# print(c.a)
d.b = "int"
# print(d.b)
e.b = "float"
# print(e.b)
#inheritance
class ClassName:
    car = "lamborghini"
    tk =  "100 crore"
    home = "something"

class ClassName1(ClassName):
    laptop = "hp"
    phone = "samsung"

a = ClassName1
# print(a.car)

class ClassName2(ClassName1,ClassName):
    standingdesk = "smart"
    dualmonitor = "Asus"
    Verticalmonitor = "..."
    Keyboard = "logitech"
    mouse = "logitech"
    pc = "gaming"
    speaker = "logitech"
    microphone = "fifine am8"
    laptop = "MacBook"
    chair = "stressable"

b = ClassName2()
c = ClassName2()
# print(b.tk, c.phone)
class classname(ClassName2):
    pass
d = classname()
# print(d.chair)
# Constructor
# class  parent:
# #
# #     def func(self,name,age):
# #         print(f"my name is {name}, my age is {age}")
# #
# # p1 = parent()
# # p1.func("Arko",12)#non paramiterized

# class parent1:
#
#     def __init__(self, name, age):
#         print(f"My name is {name}, and my age is {age}")
#
# p1 = parent1("Arko",12)# paramiterized

# polymorphism

class vehicle:
    def __init__(self,Models, Brand):
        self.Models = Models
        self.Brand = Brand

class car(vehicle):
    pass

class car1(vehicle):
    pass

x = car("i8m","BMW")
print(x.Brand,x.Models)

y = car1("Raptor","Ford Mustang")
print(y.Brand,y.Models)# vehical class has differrent thing like car & car1

class car2(vehicle):
    pass

z = car2("SUV","Corvette")
z.Models = "ZUV"#CAN BE CHANGED FOR MAKE IT UNCHANGABLE WE HAVE TO DO ENCAPSULATION.EXAMPLE IN MAIN.PY
print(z.Brand,z.Models)