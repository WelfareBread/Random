'''
Created on Oct 10, 2017

@author: andrussblack
'''

def cost_calculator():
    price2 = 0
    i = 1
    while i != 0:
        user = input("Enter a price: ")
        price = user
        price = price + price2
        price2 = price
        i = user
    final = round(price, 1)
    print(final)

def scrabble():
    scrabbleDict = {
        "E":1,"A":1,"I":1,"O":1,"N":1,"R":1,"T":1,"L":1,"S":1,"U":1,
        "D":2,"G":2,
        "B":3, "C":3,"M":3,"P":3,
        "F":4,"H":4,"V":4,"W":4,"Y":4,
        "K":5,
        "J":8,"X":8,
        "Q":10,"Z":10
        }
    user = raw_input("Enter your word: ")
    myList = []
    for i in range(len(user)):
        
        value = scrabbleDict.get(user.__getitem__(i))
        myList.append(value)
    print(myList)
    value2 = 0
    for i in range(len(myList)):
        value1 = myList.__getitem__(i)
        final_value = value1 + value2
        value2 = final_value
        
    print(final_value)


myList = [1,2,3,4,5]



        
