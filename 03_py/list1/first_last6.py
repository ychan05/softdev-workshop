def first_last6(nums):
  #checks ends for 6
  return nums[0] == 6 or nums[-1] == 6

print(first_last6([6,2,3,1,2])) #should return True
print(first_last6([0,2,3,1,5])) #should return False