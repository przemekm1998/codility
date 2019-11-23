def solution(A):
    if len(A) == 0:
        return 1

    A.sort()

    index = None

    for index, value in enumerate(A, 1):
        if index != value:
            return index

    return index + 1


def main():
    A = [1, 2, 3, 4]
    print(solution(A))

    B = []
    print(solution(B))


if __name__ == "__main__":
    main()
