class a:
    def b(self):
        print("hello world")

    @classmethod
    def d(cls):
        print("hello planet")

    @staticmethod
    def static():
        print("hello everyone")
c = a()
c.b()

c.d()
c.static()