'''
Created on Dec 14, 2017

@author: andrussblack
'''


class Human:
    
    def __init__(self, Name, Address, Age, Phone_Number):
        self.name = Name
        self.address = Address
        self.age = Age
        self.Phone_Number = Phone_Number

    def get_info(self):
        
        return self.name,self.address,self.age,self.Phone_Number

    

#H1Name, H1Address, H1Age, H1PN, H2Name, H2Address, H2Age, H2PN, H3Name, H3Address, H3Age, H3PN

def main():
    
    for i in range(3):
        if i == 0:
            o = "First"
        if i == 1:
            o = "Second"
        if i ==2:
            o = "Third"
            
        Name = input("Enter" + " " + "the" + " " +  o + " " + "Name:")
        Address = input("Enter" + " " + "the" + " " + o +  " " + "Address:")
        Age = input("Enter" + " " + "the" + " " + o +  " " + "Age:")
        Phone_Number = input("Enter" + " " + "the" + " " + o +  " " + "Phone_Number:")
        
        if i == 0:
            Human1 = Human(Name,Address,Age,Phone_Number)
        if i == 1:
            Human2 = Human(Name,Address,Age,Phone_Number)
        if i ==2:
            Human3 = Human(Name,Address,Age,Phone_Number)
            
    
    print(Human1.get_info())
    print(Human2.get_info())
    print(Human3.get_info())
    
main()


       
    
    
    






    
    