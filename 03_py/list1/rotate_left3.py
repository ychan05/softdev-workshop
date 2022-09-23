def rotate_left3(nums):
  arr = []
  for i in range(1,len(nums)):
    arr.append(nums[i])
  arr.append(nums[0])
  return arr
    
