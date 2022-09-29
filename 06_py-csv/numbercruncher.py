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
'''
import csv
import random

jobs = {} #init dict

with open('./occupations.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader) #skip heading
    for line in reader: #for every line in csv file 
        jobs[line[0]] = float(line[1]) #occupation before percentage

print(jobs)
