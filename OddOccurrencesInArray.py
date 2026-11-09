arr = [1,5,9,6,9,6,1]

def solution(A: list):
    n = len(A)
    for i in range(n):
        # if the number of instances the element appears is odd
        if A.count(A[i]) % 2 != 0:
            return A[i]
    return None

print(solution(arr))
