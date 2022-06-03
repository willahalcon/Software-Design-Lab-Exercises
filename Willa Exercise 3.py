# A simple Person class

class A:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        repr= 'Person(' + self.name + ',' + str(self.age) + ')'
        return repr

class B:
    pass
# Let's make a Person object and print the results of repr()
person = A("Willabe",20)
print(repr(person))