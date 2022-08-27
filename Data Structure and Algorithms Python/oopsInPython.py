class Animal:
    def __init__(self):
        print("Animal is Here")

    def sound(self):
        print("Animal Sounds")

class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__() # call the parent class constructor
        self.name=name
        self.breed=breed
    def getname(self):
        return self.name
    def getbreed(self):
        return self.breed
    def sound(self):
        print("Dog Barks")

class Cat(Animal):
    def __init__(self,name,breed):
        #super().__init__() # call the parent class constructor
        self.name=name
        self.breed=breed
    def getname(self):
        return self.name
    def getbreed(self):
        return self.breed
    def sound(self):
        print("Cat Meows")

def main():
    a=Animal()
    a.sound()
    d=Dog('ms','pom')
    d.sound()
    c=Cat('s','f')
    c.sound()
