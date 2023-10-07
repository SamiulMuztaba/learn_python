# global
x = 30
b = 50

# local
def func():
    global x
    a = 100
    print(a)
func()