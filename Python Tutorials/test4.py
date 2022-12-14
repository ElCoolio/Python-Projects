
# Parent Class
class Organism:
    name = "Unknown"
    species= "Unknown"
    legs= None
    arms = None
    dna = "Sequence A"
    origin = "Unknown"
    carbon_based = True

    def information(self):
        msg ="\nName : {}\nSpecies: {}\nLegs: {}\nArms: {}\nDNA: {}\nOrigin: {}\nCarbon Based: {}\n".format(self.name,self.species,self.legs,self.arms,self.dna,self.origin,self.carbon_based)
        return msg

#child class instance
class Human(Organism):
    name = "MacGuyver"
    species = "Homosapien"
    legs = 2
    arms = 2
    orgin = "Earth"

    def ingenuity(self):
        msg = "\nCreates a deadly weapon using only a paper clip, chewing gum, and a roll of duct tape!"
        return msg

class Dog(Organism):
    name = "Spot"
    species = "Canine"
    legs = 4
    arms = 0
    dna = "Sequence B"
    orgin = "Earth"

    def bite(self):
        msg = "\nEmits a loud menacing growl and bites down ferociously on it's target!"
        return msg

class Bacterium(Organism):
    name = "X"
    species = "Bacteria"
    legs = 0
    arms = 0
    dna = "Sequence C"
    orgin = "Mars"

    def replication(self):
        msg = "\nThe cells begin to divide and multiply into two seperate organisms!"
        return msg


if __name__ == "__main__":
    human = Human()
    print(human.information())
    print(human.ingenuity())

    dog = Dog()
    print(dog.information())
    print(dog.bite())

    bacteria = Bacterium()
    print(bacteria.information())
    print(bacteria.replication())
