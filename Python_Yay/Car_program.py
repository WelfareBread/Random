'''
Created on Nov 20, 2017

@author: andrussblack
'''
from Car_Class import *

Tesla = Car.__init__(2018, "Model_S")


def main():
    for i in range(5):
        Tesla.accelerate()
        print(Tesla.get_speed())
    for j in range(5):
        Tesla.brake()
        print(Tesla.get_speed())
        
        




