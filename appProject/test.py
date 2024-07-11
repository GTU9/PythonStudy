def calc(*args):
    temp=0
    for i in args:
        temp+=i
    return temp

# print(calc(1,2,3,6))

def add(**kwargs):
    temp=0
    temp=kwargs["a"]+kwargs["b"]

    return temp

# print(add(a=5,b=10))

class Car:
    def __init__(self, **kwargs):
        self.make=kwargs.get("make")
        self.color=kwargs.get("color")
        self.model=kwargs.get("model")

# my_car= Car(make="samsung",color="red")
# print(my_car.model)