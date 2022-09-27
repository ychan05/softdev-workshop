'''
TLOTFP1 Henry Bach, Donald Bi, Yat Long Chan
SoftDev
K04 -- We are picking a random devo from a krewes dictionary
2022-09-22
time spent: 1.0 hour(s)
DISCO: 
-list(d) where d is the dictionary returns the list of keys
-you can do (x,y) = [a,b] to set x to a and y to b
QCC: none
OPS SUMMARY: Randomly choose one of the keys from the given dictionary, then grab the associated list and randomly choose a devo from the elements in the list. 
'''
import random as rand

krewes = {
           2:["NICHOLAS",  "ANTHONY",  "BRIAN",  "SAMUEL",  "JULIA",  "YUSHA",  "CORINA",  "CRAIG",  "FANG MIN",  "JEFF",  "KONSTANTIN",  "AARON",  "VIVIAN",  "AYMAN",  "TALIA",  "FAIZA",  "ZIYING",  "YUK KWAN",  "DANIEL",  "WEICHEN",  "MAYA",  "ELIZABETH",  "ANDREW",  "VANSH",  "JONATHAN",  "ABID",  "WILLIAM",  "HUI",  "ANSON",  "KEVIN",  "DANIEL",  "IVAN",  "JASMINE",  "JEFFREY", "Ruiwen"], 
           7:["DIANA",  "DAVID",  "SAM",  "PRATTAY",  "ANNA",  "JING YI",  "ADEN",  "EMERSON",  "RUSSELL",  "JACOB",  "WILLIAM",  "NADA",  "SAMANTHA",  "IAN",  "MARC",  "ANJINI",  "JEREMY",  "LAUREN",  "KEVIN",  "RAVINDRA",  "SADI",  "EMILY",  "GITAE",  "MAY",  "MAHIR",  "VIVIAN",  "GABRIEL",  "BRIANNA",  "JUN HONG",  "JOSEPH",  "MATTHEW",  "JAMES",  "THOMAS",  "NICOLE",  "Karen"],
           8:["ALEKSANDRA",  "NAKIB",  "AMEER",  "HENRY",  "DONALD",  "YAT LONG",  "SEBASTIAN",  "DAVID",  "YUKI",  "SHAFIUL",  "DANIEL",  "SELENA",  "JOSEPH",  "SHINJI",  "RYAN",  "APRIL",  "ERICA",  "JIAN HONG",  "VERIT",  "JOSHUA",  "WILSON",  "AAHAN",  "GORDON",  "JUSTIN",  "MAYA",  "FAIYAZ",  "SHREYA",  "ERIC",  "JEFFERY",  "BRIAN",  "KEVIN",  "SAMSON",  "BRIAN",  "HARRY",  "Wanying", "Kevin"]
         }

#chooses num devos and returns them as a dictionary
def chooseNDevos(d,num):
    newD = {}
    for i in range(num):
        (period, devo) = chooseDevo(krewes)
        if period not in newD:
            newD[period] = [devo]
        else:
            newD[period].append(devo)
    return newD

#returns a list of a random devo and their period
def chooseDevo(d):
    pds = list(d)
    key = rand.choice(pds)
    devoList = d[key]
    return [key, rand.choice(devoList)]

#prints out period and devo
def printDevo(d):
    (period, devo) = chooseDevo(krewes)
    print((str)(period) + ": " + devo)

def toDict(l):
    l = choop

printDevo(krewes)
print(chooseNDevos(krewes,10))