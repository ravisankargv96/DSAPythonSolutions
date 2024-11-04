# Naive Approach: Using Nested loops - T.C: O(n^2) & S.C: O(1)
def productExceptSelf(arr):
    n = len(arr)
    
    # Initialize the product list as 1
    prod = [1] * n
    
    for i in range(n):
        # compute the product of all except arr[i]
        for j in range(n):
            if i != j:
                prod[i] *= arr[j]
    
    return prod

# Better Approach: Using Prefix and Suffix Array - T.C: O(n) & S.C: O(n)
"""The idea is to compute prefix and suffix products and then multiply the two products to get the result.
"""
def productExceptSelf2(arr):
    n = len(arr)
    
    # If only one element, return a list with 1
    if n == 1:
        return [1]
    
    left = [1] * n
    right = [1] * n
    prod = [1] * n
    
    # construct the left array
    for i in range(1, n):
        left[i] = arr[i-1] * left[i-1]
    
    # construct the right array
    for j in range(n-2, -1, -1):
        right[j] = arr[j+1] * right[j + 1]
    
    # construct the product array using left[] & right[]
    for i in range(n):
        prod[i] = left[i]* right[i]
    
    return prod

# Division: Using Product Array - T.C: O(n) & S.C: O(1) 
def productExceptSelf3(nums, n):
    count_zeros = 0
    prod = 1
    res = [0] * n
    
    # calculate product of all non-zero elements and count zeros
    for num in nums:
        if num == 0:
            count_zeros += 1
        else:
            prod *= num
    
    # Generate the result array
    for i in range(n):
        if count_zeros > 1:
            res[i] = 0 # entire array will be 0
        elif count_zeros == 1:
            if nums[i] == 0:
                res[i] = prod
            else:
                res[i] = 0
        else:
            res[i] = prod // nums[i] # integer division.
    
    return res

# Zero cases should be handled like above.
# Logirithm : Using Product Array - T.C: O(n) & S.C: O(1)
import math

EPS = 1e-9 #to maintain precision

def productExceptSelf4(a, n):
    
    # to hold sum of all values
    sum = 0
    for i in range(n):
        sum += math.log10(a[i])
    
    # output product for each index
    # antilog to find original product value
    for i in range(n):
        print(int(EPS + pow(10.00, sum - math.log10(a[i]))), end= " ")

    return

if __name__ == "__main__":
    arr = [10, 3, 5, 6, 2]
    res = productExceptSelf(arr)