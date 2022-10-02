'''
Ubun2 - Sebastian Ching, Yat Long Chan
SoftDev
K06 -- parse csv and weighted randoms
2022-09-29
time spent: hour(s)
DISCO: 
-
QCC:
-
HOW THIS SCRIPT WORKS:

'''
import csv
import random

occupations = {} #init dict

#parse csv
with open('./occupations.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader) #skip heading
    for line in reader: #for every line in csv file 
        occupations[line[0]] = float(line[1]) #occupation as key, percentage as value

occupations.pop('Total') #remove last line


def choose_job(occupations):
    num = int(random.random()* 999)
    for job in occupations:
        num -= int(10 * occupations[job]) #subtract weighted percentange from rand num
        if num <= 0:
            return job

test = {}
for i in range(100):
    rand = choose_job(occupations)
    if (rand not in list(test)):
        test[rand] = 1
    else:
        test[rand] += 1
print(test)