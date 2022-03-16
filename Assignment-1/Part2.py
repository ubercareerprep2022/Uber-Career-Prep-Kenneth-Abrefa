'''
Understanding
1. To get pairs of numbers that sums up to a target
    ex nums = [1,2,3,4,5] target = 7 ouput = [(2,5),(3,4)]

Plan
1. Get a new list that will keep track of the output
2.  a. loop through the items in the list
    b. substract the number from the target
    c. if the result, i.e difference, is in list then append the difference and the number that was substracted
    d. delete the number substracted from the list
3. increase the iteration of i by 1
4. return the output
'''

def pairsThatEqualSum(nums,target):
    output = []
    diff = 0
    i = 0

    while i < len(nums):
        diff = target - nums[i]

        if diff in nums:
            output.append((nums[i], diff))
            del nums[i]
        i += 1
    return output

#Testcases

# a = [1,2,3,4,5]
# b = 7

# a = [1,2,3,4,5]
# b = 5

# a = [1,2,3,4,5]
# b = 1

# a = [1,2,3,4,5]
# b = 9

# a = [-1,0,1,2,3,4,5]
# b = 0

a = [1,-2,3,4,5]
b = 3

print(pairsThatEqualSum(a,b))


