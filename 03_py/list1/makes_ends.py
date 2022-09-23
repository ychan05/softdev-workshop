def make_ends(nums):
  #list of just end chars
  return [nums[0],nums[-1]]

print(make_ends([5,2,3,1])) #[5,1]
print(make_ends([6,44,2,6,7])) #[6,7]