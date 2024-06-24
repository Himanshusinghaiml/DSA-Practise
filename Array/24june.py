# Q 2. Find the Duplicate Number
# Given an array of integers nums containing n + 1 integers where each integer
# is in the range [1, n] inclusive.
# There is only one repeated number in nums, return this repeated number.
# You must solve the problem without modifying the array nums and uses only
# constant extra space.
# Example 1:
# Input:
def find_duplicate(nums):
    # Define the search range
    low = 1
    high = len(nums) - 1
    
    while low < high:
        mid = (low + high) // 2
        count = sum(x <= mid for x in nums)
        
        if count > mid:
            high = mid
        else:
            low = mid + 1
    
    return low


nums = [1, 3, 4, 2, 2]
duplicate_number = find_duplicate(nums)
print("The duplicate number is:", duplicate_number)


