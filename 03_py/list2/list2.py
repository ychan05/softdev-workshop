#1
def count_evens(nums):
  # We create a count variable to keep track of the number
  count = 0
  # We look at each item in nums
  for i in nums :
    # We check if its even and inrease count if it is
    if i % 2 == 0 :
      count += 1
  return count

print(count_evens([2,2,0,5,7])) # Should return 3
print(count_evens([1,1,1,7,-2])) # Should return 1

#2
def big_diff(nums):
    # We set the starting values for max/min
    max_val = nums[0]
    min_val = nums[0]
    # We look at each item in nums
    for i in nums :
        # We update the new max/min
        if i > max_val :
            max_val = i
        if i < min_val :
            min_val = i
    # We return the difference
    return max_val-min_val;

print(big_diff([2,3,7,0])) # Should return 7
print(big_diff([1])) # Should return 0

#3
def centered_average(nums):
    # We set the starting values for max/min
    max_val = nums[0]
    min_val = nums[0]
    # We look at each item in nums
    for i in nums :
        # We update the new max/min
        if i > max_val :
            max_val = i
        if i < min_val :
            min_val = i
    # We find and return the total
    total = 0-max_val-min_val
    for i in nums :
        total += i
    return total/(len(nums)-2);

print(centered_average([15, 4, 6, 0])) # Should return 5
print(centered_average([-100, -100, 100])) # Should return -100

#4
def sum13(nums):
    total = 0
    # Create a variable to track if the last number is 13
    past13 = False
    # We look at each item in nums
    for i in range(len(nums)) :
        # If it's 13, ignore it and set the last number to 13
        if nums[i] == 13 :
            past13 = True
        # If the last number is 13, ignore it
        elif past13 :
            past13 = False
        #Otherwise add it to the total
        else :
            total += nums[i]
    return total

print(sum13([13,1,1,1,7,0])) # Should return 9
print(sum13([9, 13, 13, 4, 8])) # Should return 17

#5
def sum67(nums):
    total = 0
    # Create a variable to track if there's been a 6
    past6 = False
    # We look at each item in nums
    for i in nums :
        # If it's a 7, ignore it and turn off past6
        if i == 7 and past6:
            past6 = False
        # If it's a 6, tgnore it and turn off past6
        elif i == 6 :
            past6 = True
        # If there's been a 7 but not a 6 ignore it, otherwise add it
        elif not past6 :
            total += i
    return total

print(sum67([6,7,0,9,6,6,8,9,7])) # Should return 9
print(sum67([7,8,2,14])) # Should return 31

#6
def has22(nums):
    # Check if the array is too small
    if len(nums) <= 1 :
        return False
    # Look at each item but the last in nums
    for i in range(len(nums)-1) :
        # Check if the next is a 2 and return true if that's the case
        if nums[i] == 2 and nums[i+1] == 2 :
            return True
    # If not, return false
    return False

print(has22([1,4,6,2,5,8,2,2,8,9])) # Should return True
print(has22([2,5,43,2,-2,2,8])) # Should return False
  




