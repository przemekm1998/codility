def split_sum(A):
    head = A[0]
    tail = sum(A[1:])
    min_diff = abs(head - tail)
    for i in range(1, len(A) - 1):
        head += A[i]
        tail -= A[i]
        temp_diff = abs(head - tail)
        min_diff = min(min_diff, temp_diff)
    return min_diff
