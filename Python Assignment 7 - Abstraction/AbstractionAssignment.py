from abc import ABC, abstractmethod #this import is essential to using abstraction

class Animal: #parent class, most variables are placeholders
    name = "None Provided"
    animalia = " "
    diet = " "
    numOfLegs = None
    topSpeed = None
    call = " "
    
    @abstractmethod #this defines information as an abstract method.  
    def information(ABC):
        pass

    def callSound(self):
        msg ="The {} goes {}".format(self.name, self.call)
        return msg

class Cat(Animal): #child class, inherited variables are overwritten with new values.  Has additional property of hasTail
    name = "Cat"
    diet = "carnivore"
    animalia = "vertibrate"
    numOfLegs = 4
    topSpeed = 30
    hasTail = True
    call = "Meow!"


    def information(self): #Since the information function is unique for each animal, we defined the implementation in the child class
        msg ="\nName : {}\nAnimalia: {}\nDiet: {}\nTop Speed: {}\nNumber of Legs {}".format(self.name,self.animalia,self.diet,self.topSpeed,self.numOfLegs)
        return msg

    def pounce(self):
        msg = "The cat pounces on its prey!"
        return msg

class Bird(Animal): #child class, inherited variables are overwritten with new values.  Has additional property of numOfWings and flightSpeed.
    name = "Bird"
    diet = "herbivore"
    animalia = "vertibrate"
    numOfLegs = 2
    numOfWings = 2
    topSpeed = 1
    flightSpeed = 40
    call = "Chirp!"

    def information(self): #Since the information function is unique for each animal, we defined the implementation in the child class
        msg ="\nName : {}\nAnimalia: {}\nDiet: {}\nTop Speed: {}\nFlight Speed: {}".format(self.name,self.animalia,self.diet,self.topSpeed,self.flightSpeed)
        return msg

    def fly(self):
        msg = "The bird flys high into the sky!"
        return msg
    
    
if __name__ == "__main__":
    cat = Cat()
    print(cat.information())
    print(cat.callSound())
    print(cat.pounce())

    bird = Bird()
    print(bird.information())
    print(bird.callSound())
    print(bird.fly())
