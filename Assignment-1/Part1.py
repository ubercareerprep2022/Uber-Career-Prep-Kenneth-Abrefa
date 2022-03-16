'''
Understanding
1. For s1 to be a permutation of s2:
    a. all elements in s1 must be in s2
    b. there shouldn't be any extra character between in between s1 when represented in s2
        ex. s1 = "asfd" is not a permutation of s2= "asd"
Match
Using dictionaries will be an effective way of solving this problem since it helps us keep
track of the item and the number of times it has appeared in the string

Plan
1. initialize a left and right point
    a. helps us pass items in s2 to dictionary while checking if conditions have been met
2. will use the counter functiont to keep track of items in both strings
3. for the 2nd dictionary i will first pass element in range from left to right
    then gradually add or delete elements depending of the stated.
4. will then return false if the program runs without meeting the intial true condition
'''

from collections import Counter
def isStringPermutation(s1, s2):
    # initialize a left and right pointer that will help me pass element in s2 into the dictionary
    left = 0
    right = len(s1)-1

    #Counter used to get items in s1 into the dictionary
    #with values assigned to the keys
    #dictionary 2 stores the values of element from index 0 to the right-1
    dic_s1 = Counter(s1)
    dic_s2 = Counter(s2[left:right])


    while right < len(s2):
        # keep addding elements to dictionary 2
        # until there are no more elements to be added
        # or a condition has been met
        dic_s2[s2[right]] += 1

        if dic_s1 == dic_s2:
            return True

        else:
            # reduce the value of dictionary key at index 0 by 1
            dic_s2[s2[left]] -= 1
            
            # delete the key from the dictionary of the value is 0
            if dic_s2[s2[left]] == 0:
                del dic_s2[s2[left]]
        left += 1
        right += 1
    
    
    return False

#Testcases

a = "asdf"
b = "asf"

# a = "adc"
# b = "dcda"

# a = "ab"
# b = "kibaitoa"

print(isStringPermutation(a,b))

#Time complexity -> O(N)
#Space complexity -> O(N)