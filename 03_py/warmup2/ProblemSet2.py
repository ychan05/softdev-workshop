#2-1
def string_times(str, n):
    return str * n #We can multiply strings in Python
print("=======string_times=======")
print(string_times("Hi",2))
print(string_times("Hi",3))


#2-2
def front_times(str, n):
    if len(str) < 3 : #if the str is shorter than 3 characters, the front is the string itself
        front = str
    else :
      front = str[:3] #Otherwise, take the first 3 chars
    return front*n #multiply the front n times
print("=======front_times=======")
print(front_times('Chocolate', 2))
print(front_times('Chocolate', 3))
print(front_times('Ch', 2))
#2-3
def string_bits(str):
    return str[::2] # We can use :: to skip every second char in a string
print("=======string_bits=======")
print(string_bits("hello"))
print(string_bits("hi"))

#2-4
def string_splosion(str):
    result = ""
    for i in range(len(str)):
        result += str[:i] #adds substring up to index i to result
    return result + str 
print("=======string_splosion=======")
print(string_splosion("abba"))
print(string_splosion("code"))

#2-5
def last2(str):
    if len(str) < 2: #if length < 2, string is too short
        return 0
    count = 0
    for i in range(len(str)-2):
        if str[i:i+2] == str[-2:]: #check if each substring is equal to the last 2 chars 
            count += 1
    return count
print("=======last2=======")
print(last2("hixxhi"))
print(last2("axxxaaxx"))

#2-6
def array_count9(nums):
    count = 0
    #iterate through array and check for 9s
    for i in nums:
        if i == 9:
            count += 1
    return count
print("=======array_count9=======")
print(array_count9([1, 2, 9]))
print(array_count9([9,9,9,9]))

#2-7
def array_front9(nums):
    #if len is < 4, iterate through length of array, otherwise iterate through first 4 elements
    for i in range(min(len(nums),4)):
        if nums[i] == 9: #return True if one of the first elements is a 9
            return True;
    return False;
print("=======array_front9=======")
print(array_front9([1, 2, 9, 3, 4]))
print(array_front9([1, 2, 5, 3, 4]))
print(array_front9([1, 2, 9])) 


#2-8
def array123(nums):
    #iterate through array
    for i in range(len(nums) - 2):
        #check each sequence of 3 numbers
        if nums[i]== 1 and nums[i+1]== 2 and nums[i+2]== 3:
            return True
    return False
print("=======array123=======")
print(array123([1, 1, 2, 3, 1]))
print(array123([1, 1, 2, 4, 1]))


#2-9
def string_match(a, b):
  count = 0
  #iterate until end of shorter string
  for i in range(min(len(a),len(b))-1):
    if (a[i:i+2] == b[i:i+2]): #check if substrings match
      count += 1
  return count
print("=======string_match=======")
print(string_match('xxcaazz', 'xxbaaz'))
print(string_match('abc', 'cab'))


    