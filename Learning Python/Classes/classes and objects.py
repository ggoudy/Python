# Create a Class

class thisismyclass:
    x = 15
    y = 10
# Create a Object
p1 = thisismyclass()
print(p1.x * p1.y)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

myname = input("Please type your name: ")
myage = int(input("Please type your age: "))
p2 = Person(myname, myage)

print(p2.name)
print(p2.age)

