def solution(X, Y, D):
    import math

    steps = (Y - X) / D

    return math.ceil(steps)


def main():
    X = 10
    Y = 85
    D = 30
    print(solution(X, Y, D))


if __name__ == "__main__":
    main()
