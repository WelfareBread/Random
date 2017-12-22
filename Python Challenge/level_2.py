'''
Created on Nov 28, 2017

@author: andrussblack
'''
import urllib

mess = urllib.request("http://www.pythonchallenge.com/pc/def/ocr.html").read().decode()

print(mess)
