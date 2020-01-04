def solution(X, A):
    path_sum = (X * (X + 1)) / 2
    duplicated = dict()

    for i in range(0, len(A)):
        if A[i] not in duplicated and A[i] <= X:
            path_sum -= A[i]
            duplicated[A[i]] = 1
            if path_sum == 0:
                return i
    return -1
