'''
Created on Oct 12, 2017

@author: andrussblack
'''

import turtle
turt = turtle.Turtle()

def point(X,Y,LeftBound,Rightbound,Lowerbound,UpperBound):
    unitX = 350/(Rightbound-LeftBound)
    unitY = 340/(UpperBound-Lowerbound)
    turt.forward(X*unitX)
    turt.left(90)
    turt.forward(Y*unitY)
    


    

    
point(5,5,-10,10,-10,10)

    
    