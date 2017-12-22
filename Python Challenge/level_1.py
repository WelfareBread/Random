'''
Created on Nov 28, 2017

@author: andrussblack
'''
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c",".",".","."," "," "," ","(","(","(",")",")",")","'","'","'"]

def decrypt(ET):
    Final = ""
    for i in range(len(ET)):
       
        a = alphabet.index(ET.__getitem__(i))
        b = a + 2
        
        Final = Final + alphabet.__getitem__(b)
        
    print(Final)

        
    
    
decrypt("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.")
