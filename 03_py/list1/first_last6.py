def first_last6(nums):
  return nums[0] == 6 or nums[len(nums)-1] == 6

print(first_last6([6,2,3,1,2])) #should return True
print(first_last6([0,2,3,1,5])) #should return False