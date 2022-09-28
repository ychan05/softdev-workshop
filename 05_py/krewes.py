'''
Sebastian Ching, Yat Long Chan
SoftDev
K05 -- Random devo from .txt file
2022-09-28
time spent: 1.0 hour(s)
DISCO: 
- Map a key to a list if you want to store multiple values to a single key
QCC: none
'''
import random
krewes_list = open('krewes.txt','r') #open krewes.txt file
krewes_list = krewes_list.read().strip() #turn file obj to str and remove trailing/leading whitespaces
krewes_list = krewes_list.split('@@@') #split str into list of period$$$devo$$$ducky

krewes = {} #init dict
print(krewes_list)

#txt file -> dictionary
for i in krewes_list:
    if len(i) != 0: #ignore last item
        tmp = i.split('$$$') #split each item into [period, devo, ducky]
        period = (tmp[0]) #period always first item in list
        devo = [(tmp[1], tmp[2])] #devo and duck in a tuple. Always 2nd and 3rd item 
        if period not in krewes:
            krewes[period] = devo
        else:
            krewes[period].append(devo)