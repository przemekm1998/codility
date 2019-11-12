"""
BINARY GAP
"""


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    import re

    num = bin(N)[2:]
    print(str(num))

    r1 = re.match("10+1", num)

    if (r1 != None):
        print(r1.span()[1])

    # print(r1)
    # num = num[6:]
    # r1 = re.match("10+1",num)
    # print(r1)

solution(1041)
