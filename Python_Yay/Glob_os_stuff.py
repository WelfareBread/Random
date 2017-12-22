'''
Created on Nov 2, 2017

@author: andrussblack
'''
import turtle
import os
import glob

def star():
    turt = turtle.Turtle()
    turt.forward(50)
    for i in range(5):
        
        turt.right(144)
        turt.forward(100)

def MilesPerGallon(Miles_Driven, Gallons_Used):
    MPG = Miles_Driven/Gallons_Used
    print(MPG)

def Cookies(Number_of_Cookies):
    CoS = 1.5
    CoB = 1             #for 48 cookies
    CoF = 2.75
    print(CoS*(Number_of_Cookies/48), "Cups of Sugar", CoB*(Number_of_Cookies/48), "Cups of Butter", CoF*(Number_of_Cookies/48), "Cups of Flour")
    
def pyFiles():
    os.chdir("/Users/andrussblack/Desktop/Test")
    print(glob.glob("/Users/andrussblack/Desktop/Test/*.py"))
    
pyFiles()    


    

            
        
     


    
