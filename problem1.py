# Given a list of integers and a target number,
# return the indices of two numbers such that they add up to the target.

def indexreturner(givennums, target):
    for i in range(len(givennums) - 1):
        for j in range(i + 1, len(givennums)):
            if givennums[i] + givennums[j] == target:
                print(f"The indices to achieve {target} are {i} and {j}")
                return (i, j)

# Example
nums = [2, 7, 11, 15]
target = 9
indexreturner(nums, target)
