# 1-1
def sleep_in(weekday, vacation):
  #not weekday means weekend => sleep in on vacation and weekends
  if (vacation or not weekday) :
    return True
  return False

print("sleep_in test1:" + sleep_in(True,True)) #True
print("sleep_in test2:" + sleep_in(False,False)) #True
print("sleep_in test3:" + sleep_in(True,False)) #False

#1-2
def monkey_trouble(a_smile, b_smile):
  #checks if the monkeys are both smiling or not
  if (a_smile and b_smile or not a_smile and not b_smile) :
    return True
  return False

print("monkey_trouble test1:" + monkey_trouble(True,True)) #True
print("monkey_trouble test2:" + monkey_trouble(False,False)) #True
print("monkey_trouble test3:" + monkey_trouble(True,False)) #False

#1-3
def sum_double(a, b):
  #4*a is the same as double the sum of a and b if they are the same
  if a == b :
    return 4*a
  return a+b

print("sum_double test1:" + sum_double(2,2)) #8
print("sum_double test2:" + sum_double(5,4)) #9

#1-4
def diff21(n):
  #doubles absolute difference when n is greater than 21
  if n > 21 :
    return (n-21)*2
  return 21-n

print("diff21 test1:" + diff21(25)) #8
print("diff21 test2:" + diff21(5)) #16

#1-5
def parrot_trouble(talking, hour):
  #we are only not in trouble in between hours 7 and 20 when parrot talks
  if (hour < 7 or hour > 20) and talking :
    return True
  return False

print("parrot_trouble test1:" + parrot_trouble(True,4)) #True
print("parrot_trouble test2:" + parrot_trouble(True,12)) #False
print("parrot_trouble test3:" + parrot_trouble(False,4)) #False

#14t
def makes10(a, b):
  #either a,b or a+b is 10
  return a == 10 or b== 10 or a+b == 10

print("makes10 test1:" + makes10(10,3)) #True
print("makes10 test2:" + makes10(2,10)) #True
print("makes10 test3:" + makes10(7,3)) #True
print("makes10 test4:" + makes10(2,3)) #False

#1-7
def near_hundred(n):
  #distance between 100 or 200 is less than or equal to 10
  return abs(n-100) <= 10 or abs(n-200) <= 10

print("near_hundred test1:" + near_hundred(105)) #True
print("near_hundred test2:" + near_hundred(140)) #False
print("near_hundred test3:" + near_hundred(210)) #True
print("near_hundred test4:" + near_hundred(250)) #False

#1-8
def pos_neg(a, b, negative):
  #negative and both negative or not negative and only one is negative
  return negative and a < 0 and b < 0 or not negative and (a < 0 and b > 0 or a > 0 and b < 0)

print("pos_neg test1:" + pos_neg(5,-4,False)) #True
print("pos_neg test2:" + pos_neg(-5,-7,True)) #True
print("pos_neg test3:" + pos_neg(4,4,False)) #False
print("pos_neg test4:" + pos_neg(-5,4,True)) #False

#1-9
def not_string(str):
  #adds not to front if it doesn't have
  if str[:3] == "not" : 
    return str
  return "not "+str

print("not_string test1:" + not_string("candy")) #not candy
print("not_string test2:" + not_string("not sky")) #not sky

#1-10
def missing_char(str, n):
  #[:n] gets everything before n, [n+1:] gets everything after
  return str[:n]+str[n+1:]

print("missing_char test1:" + missing_char("candy",3)) #cany
print("missing_char test2:" + missing_char("not sky",2)) #no sky

#1-11
def front_back  (str):
  if len(str) <= 1:
    return str
  
  #[-1] for last char, [1:-1] for middle part, [0] to add back the first char
  return str[-1]+str[1:-1]+str[0]

print("front_back test1:" + front_back("candy")) #yandc
print("front_back test2:" + front_back("not sky")) #yot skn

#1-12
def front3(str):
  #checks for string length
  if len(str) < 3 :
    front = str
  else :
    front = str[:3]
  return front*3

print("front3 test1:" + front3("candy")) #cancancan
print("front3 test2:" + front3("not sky")) #notnotnot
print("front3 test1:" + front3("ye")) #yeyeye



