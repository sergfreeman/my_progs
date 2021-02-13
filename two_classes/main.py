class Base:

    def method(self, msg):
        print(msg)
        return


class Child(Base):
    pass


b = Base()
b.method("Hello from Base")

c = Child()
c.method("Hello from Child")