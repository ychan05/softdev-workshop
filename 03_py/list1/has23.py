from re import A


def has23(nums):
  #checks for 3 in either index
  return nums[0] == 2 or nums[0] == 3 or nums[1] == 2 or nums[1] == 3

print(has23([6,4])) #False
print(has23([2,1])) #True
print(has23([6,3])) #True