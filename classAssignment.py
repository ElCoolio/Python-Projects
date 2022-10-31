class Animal: #parent class, most variables are placeholders
    name = "None Provided"
    animalia = " "
    diet = " "
    numOfLegs = 0
    topSpeed = 0

class Cat(Animal): #child class, inherited variables are overwritten with new values.  Has additional property of hasTail
    diet = "carnivore"
    animalia = "vertibrate"
    numOfLegs = 4
    topSpeed = 30
    hasTail = True

class Bird(Animal): #child class, inherited variables are overwritten with new values.  Has additional property of numOfWings and flightSpeed.
    diet = "herbivore"
    animalia = "vertibrate"
    numOfLegs = 2
    numOfWings = 2
    topSpeed = 1
    flightSpeed = 40
    
    
