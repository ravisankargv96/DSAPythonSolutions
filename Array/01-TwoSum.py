# Naive approach - T.C. O(n^2) & S.C. O(1)
def twoSum(arr, target):
    res = []
    
    # check all possible pairs
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            
            # If sum of current pair is equal
            # to target then copy it to result
            if arr[i] + arr[j] == target:
                res = [arr[i], arr[j]]
                return res
    
    return res 

# Note: This approach is only advicable if you need arr[i] & arr[j]; not for i & j
# Sorting & Binary Search -> T.C: O(n* log(n)) S.C: O(1)
# Algo: Binary Search

# Function: arr[ind] == target ? return ind : return -1
# args: arr, range (lo, hi), tar
def binarySearch(arr, lo, hi, target):
    while lo <= hi:
        mid = lo + (hi - lo)
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

def twoSum2(arr, target):
    n = len(arr)
    res = []
    
    arr.sort()
    
    for i in range(n):
        search = target - arr[i]
        
        idx = binarySearch(arr, i+1, n-1, search)
        if idx != -1: 
            res = [arr[i], arr[idx]]
            return res
    
    return res

# Note: This approach is only advicable if you need arr[i] & arr[j]; not for i & j
# Sorting and Two Pointers - T.C: O(n*log(n)) S.C: O(1)
# Algo: TwoPointer

def twoSum3(arr, target):
    res = []
    arr.sort()
    
    left = 0
    right = len(arr) - 1
    
    # Iterate while left pointer is less than right
    while left < right:
        sum = arr[left] + arr[right]
        
        # check if sum matches target
        if sum == target:
            res = [arr[left], arr[right]]
            break
        elif sum < target:
            left += 1
        else:
            right -= 1
    return res

# Expected Approach: Using HashSet - T.C: O(n) S.C: O(n)
def twoSum4(arr, target):
    res = []
    
    st = set()
    
    for i in range(len(arr)):
        search = target - arr[i]
        
        if search in st:
            res = [target, arr[i]]
            return res
         
        st.add(arr[i])
    
    return res

if __name__ == "__main__":
    arr = [2, 9, 10, 4, 15]
    target = 12
    
    res = twoSum(arr, target)
    
    for x in res:
        print(x, end=" ")