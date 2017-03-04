A = [1,5,4,8,2,-1,6]
B = [-1,-5,-4,-3,-9,-4,-8,-2]

def memoized(A):
    for i in len(A):
        if i == 0:
            return 0
        if A[i] is empty:
            A[i] = max(memoized(i-1) + A[i],A[i])
        
def iterative(A):
    best_max = A[0]
    current_max = A[0]
    for i in range(1,len(A)):
        current_max = max(A[i],current_max+A[i])
        best_max = max(best_max,current_max)
    return best_max

print("mem= ",memoized(A))
print("iter= ",iterative(A))

print("mem= ",memoized(B))
print("iter= ",iterative(B))
