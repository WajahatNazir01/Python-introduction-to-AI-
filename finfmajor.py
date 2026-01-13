def find_majority(nums):
    candidate = None
    count = 0

    for num in nums:
        # If count is 0, we pick a new candidate
        if count == 0:
            candidate = num
        
        # If the current number is our candidate, increase count
        # If it's different, decrease count (they 'fight')
        if num == candidate:
            count += 1
        else:
            count -= 1
            
    return candidate

# Test
print(find_majority([2, 2, 1, 1, 1, 2, 2])) # Output: 2