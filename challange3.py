def solution(A, K):
    array_length = len(A)

    if array_length == 0:
        return A

    if K > array_length:
        K = K % array_length

    new_array = [None] * array_length

    for i in range(0, array_length):
        if i + K < array_length:
            new_array[i + K] = A[i]
        else:
            index = (i + K) - array_length
            new_array[index] = A[i]

    return new_array


def main():
    A = [2, 2, 3, 3, 4]
    K = 2
    print(solution(A, K))


if __name__ == "__main__":
    main()
