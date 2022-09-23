def sum2(nums):
  #checks lengths
  if len(nums) == 0:
    return 0
  if len(nums) == 1:
    return nums[0]
  #default case sums first two elements
  return nums[0] + nums[1]

print(sum2([])) #0
print(sum2([5])) #5
print(sum2([4,2])) #6
print(sum2([1,5,2,3])) #6