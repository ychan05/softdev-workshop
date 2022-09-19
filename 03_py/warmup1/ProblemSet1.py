# 1-1
def sleep_in(weekday, vacation):
  if (vacation or not weekday) :
    return True
  return False

#1-2
def monkey_trouble(a_smile, b_smile):
  if (a_smile and b_smile or not a_smile and not b_smile) :
    return True
  return False

#1-3
def sum_double(a, b):
  if a == b :
    return 4*a
  return a+b

#1-4
def diff21(n):
  if n > 21 :
    return (n-21)*2
  return 21-n

#1-5
def parrot_trouble(talking, hour):
  if (hour < 7 or hour > 20) and talking :
    return True
  return False

#1-6
def makes10(a, b):
  return a == 10 or b == 10 or a+b == 10

#1-7
def near_hundred(n):
  return abs(n-100) <= 10 or abs(n-200) <= 10

#1-8
def pos_neg(a, b, negative):
  return negative and a < 0 and b < 0 or not negative and (a < 0 and b > 0 or a > 0 and b < 0)

#1-9
def not_string(str):
  if str[:3] == "not" : 
    return str
  return "not "+str

#1-10
def missing_char(str, n):
  return str[:n]+str[n+1:]

#1-11
def front_back(str):
  if len(str) <= 1:
    return str
  return str[-1]+str[1:-1]+str[0]

#1-12
def front3(str):
  if len(str) < 3 :
    front = str
  else :
    front = str[:3]
  return front*3




