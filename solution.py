# In a given integer array A, we must move every element of A to either list B or list C. (B and C initially start
# empty.)
#
# Return true if and only if after such a move, it is possible that
# the average value of B is equal to the average value of C, and B and C are both non-empty.
#
# Sample input:
# [1,2,3,4,5,6,7,8]
# Sample output:
# True

# Explanation: We can split the array into [1,4,5,8] and [2,3,6,7], and both of them have the average of 4.5.
#
# Note:
# - The length of A will be in the range [1, 30].
# - A[i] will be in the range of [0, 10000].

"""
Function that checks if an array can be split into two lists with the same average of elements
@:param A: List[int]
@:return: bool, true if the condition is met, otherwise false
"""


def splitArraySameAverage(A):
    def possible(n, s):
        for i in range(1, n // 2 + 1):
            if s * i % n == 0:
                return True
        return False

    n = len(A)
    s = sum(A)
    if not possible(n, s):
        return False

    sums = [set() for _ in range(n // 2 + 1)]
    sums[0].add(0)

    for i in A:
        for j in reversed(range(1, n // 2 + 1)):
            for prev in sums[j - 1]:
                sums[j].add(prev + i)

    for i in range(1, n // 2 + 1):
        if s * i % n == 0 and s * i // n in sums[i]:
            return True
    return False


def run():
    a = []

    # number of elements as input
    n = int(input("Enter number of elements: "))

    for i in range(0, n):
        elem = int(input("Element " + str(i + 1) + ": "))
        a.append(elem)  # adding the element

    ok = splitArraySameAverage(a)
    print(ok)


run()
