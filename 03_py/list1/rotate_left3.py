def rotate_left3(nums):
  arr = []
  for i in range(1,len(nums)):
    arr.append(nums[i]) #makes a new list with every element except 0 index
  arr.append(nums[0]) #adds 0 index element
  return arr

print(rotate_left3([5,4,3])) #[4,3,5]
print(rotate_left3([7,2,6])) #[2,6,7]
    
