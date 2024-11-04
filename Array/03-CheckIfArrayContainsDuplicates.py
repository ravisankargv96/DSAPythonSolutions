# Note: Here the optimal might be sorting, but exploring other Algos also.
# Naive Approach: Using 2 nested loops - T.C: O(n^2) S.C: O(1)
def check_duplicates(arr):
    n = len(arr)
    
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] == arr[j]:
                return True
    
    return False

# Other Approach: By Sorting Array - T.C: O(n*log(n)) S.C: O(1)
def check_duplicates2(arr):
    n = len(arr)
    
    arr.sort()
    
    for i in range(n-1):
        if arr[i] == arr[i+1]:
            return True
        
    return False


# Expected Approach: Using HashSet - T.C: O(n) S.C: O(n)
def check_duplicates3(arr):
    n = len(arr)
    
    st = set()
    
    for i in range(len(arr)):
        if arr[i] in st:
            return False
        st.add(arr[i])

    return False

if __name__ == "__main__":
    arr = [4, 5, 6, 4]
    print(check_duplicates(arr))
