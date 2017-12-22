'''
Created on Nov 14, 2017

@author: andrussblack
'''
class Pet:
    
    def __init__(self):
        self.name = "Darthor"
        self.animalType = "Cat"
        self.age = 4
        
    def setName(self, Name):
        self.name = Name
        
    def setAnimalType(self, AnimalType):
        self.animalType = AnimalType
        
    def setAge(self, Age):
        self.age = Age
        
    def getName(self):
        return self.name
    
    def getAnimalType(self):
        return self.animalType
    
    def getAge(self):
        return self.age
    

    

    

