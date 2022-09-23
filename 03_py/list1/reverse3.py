from audioop import reverse
import re


def reverse3(nums):
  arr = []
  for i in range(1,len(nums)): 
    arr.append(nums[-1*i]) #adds elements from index 1 in reverse order
  arr.append(nums[0]) #adds the previous 0 index element at the end
  return arr

print(reverse3([3,2,5])) #[5,2,3]
print(reverse3([6,5,4])) #[4,5,6]
    
