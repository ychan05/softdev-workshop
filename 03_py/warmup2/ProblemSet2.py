#2-1
def string_times(str, n):
    return str * n

#2-2
def front_times(str, n):
    if len(str) < 3 :
        front = str
    else :
      front = str[:3]
    return front*n

#2-3
def string_bits(str):
    return str[::2]

#2-4
def string_splosion(str):
    result = ""
    for i in range(len(str)):
        result += str[:i]
    return result + str

#2-5
def last2(str):
    count = 0
    for i in range(len(str)-2):
        if str[i:i+2] == str[-2:]:
            count += 1
    return count

#2-6
def array_count9(nums):
    count = 0
    for i in nums:
        if i == 9:
            count += 1
    return count

#2-7
def array_front9(nums):
    for i in range(min(len(nums),4)):
        if nums[i] == 9:
            return True;
    return False;

#2-8
def array123(nums):
    number = 0
    for i in nums:
        if i == 1:
            number = 1
        elif i == 2 and number == 1:
            number += 1
        elif i == 3 and number == 2:
            return True
        else :
            number = 0
    return False

#2-9
def string_match(a,b):
    