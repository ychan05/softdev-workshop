'''
Ubuntwo - Sebastian Ching, Yat Long Chan
SoftDev
K06 -- parse csv and weighted randoms
2022-09-29
time spent: 1 hour(s)
DISCO: 
- Our frequency fxn generates more accurate data when using larger sample sizes
QCC:
- Why is the total percentage out of 99.8?

HOW THIS SCRIPT WORKS:

Weighted random algo:
1. Generate number from [0,99.8]
2. Iterate through all percentages and subtract from random number
3. When random number <= 0, return current job

frequency algo:
1. create a new dict for frequencies
2. fill dict with occupations
3. generate random job, then increment the frequency of that job
4. repeat step 3 n times
5. for each job in dict, divide freq by n and multiply by 100 for percentage
6. return dict
'''
import csv
import random

occupations = {} #init dict

#parse csv
with open('./occupations.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader) #skip heading
    for line in reader: 
        occupations[line[0]] = float(line[1]) #occupation as key, percentage as value

occupations.pop('Total') #remove last line

#randomly choose a job from list of occupations
def choose_job(occupations):
    num = random.random()* 99.8
    for job in occupations:
        num -= occupations[job] #subtract weighted percentange from rand num
        if num <= 0:
            return job


#used to test accuracy of our weighted random fxn
#more accurate w/ larger sample size
def get_frequencies(n):
    freq = {} #dict of jobs and frequencies
    
    for job in occupations: 
        freq[job]= 0 #add keys to dict
    
    for i in range(n):
        rand_job = choose_job(occupations)
        freq[rand_job]+= 1 #add to frequency of chosen job
    
    for job in occupations:
        freq[job] =  (freq[job]/n)*100 #percentage of frequencies 

    return freq

print(choose_job(occupations))
#print(get_frequencies(1000000))