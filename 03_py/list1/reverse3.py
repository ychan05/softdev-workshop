def reverse3(nums):
  arr = []
  for i in range(1,len(nums)):
    arr.append(nums[-1*i])
  arr.append(nums[0])
  return arr
    
