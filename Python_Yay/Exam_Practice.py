'''
Created on Dec 13, 2017

@author: andrussblack
'''
salesList = []

class CashRegister:
    
    def purchase_item(self):
        salesList.append(self)
        
    def get_total(self):
        
        total = 0
        
        for i in range(len(salesList)):
            
            a = salesList.__getitem__(i)
            total = a.price + total
            
        print(total)
    

class RetailItem(CashRegister):
    
    def __init__(self,item_description, units_in_inventory, price):
        self.ID = item_description
        self.UII = units_in_inventory
        self.price = price
        
    
        
def main(Item1, Item2, Item3):
    Item1 = RetailItem("Jacket",12,59.95)
    Item2 = RetailItem("Designer Jeans",40,34.95)
    Item3 = RetailItem("Shirt",20,24.95)
   
    Item1.purchase_item()
    Item2.purchase_item()
    Item3.purchase_item()
    
    Item1.get_total()
    
    
main("Jacket","Jeans","Shirt")
    

    

    


    