'''
Created on Nov 16, 2017

@author: andrussblack
'''
class Car:
    
    def __init__(self,year_model,make):
        self.year_model = year_model
        self.make = make
        self.speed = 0
        
        
    def accelerate(self):
        self.speed + 5
    
    def brake(self):
        self.speed - 5
        
    def get_speed(self):
        return self.speed