"""
BINARY GAP
"""

import re


def solution(number):

    num = bin(number)[2:]
    stop = False
    longest_count = 0

    while not stop:
        r1 = re.search("10+1", num)

        if r1 is not None:

            match_length = len(r1.group())
            binary_gap = match_length - 2

            if binary_gap > longest_count:
                longest_count = binary_gap

            endpoint = r1.span()[1] - 1
            num = num[endpoint:]

        else:
            stop = True

    return longest_count


def main():
    number = 1041 # pass number to test
    print(solution(number))


if __name__ == "__main__":
    main()
