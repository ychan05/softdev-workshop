def max_end3(nums):
  #uses max() to find bigger value of the two
  big = max(nums[0],nums[2])
  nums = [big,big,big]
  return nums

print(max_end3([2,5,1])) #[2,2,2]
print(max_end3([3,4,8])) #[8,8,8]