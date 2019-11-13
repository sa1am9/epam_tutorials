import sys


"""
Function for search "Largest common sequence".
Make only for 2 sequence.
Because it’s easier to call the function 2 times,
    than to think about the variables later.
"""


def lcs_recursive(x, y):
    if len(x) == 0 or len(y) == 0:
        return []

    if x[-1] == y[-1]:
        return lcs_recursive(x[:-1], y[:-1]) + [x[-1]]

    else:
        left = lcs_recursive(x[:-1], y)
        right = lcs_recursive(x, y[:-1])
        return left if len(left) > len(right) else right


"""
Function for verify lens between 
input len and len of seq. 
No longer came up with why we need this length.
"""


def verify_len(n, seq):
    if n != len(seq):
        print("Incorrect input data for {} seq. Its len does not coincide".format(seq))
        sys.exit()


if __name__ == "__main__":

    n1 = int(input("n1 -- "))
    seq1 = input("sequence first - ").split(" ")
    verify_len(n1, seq1)
    n2 = int(input("n2 -- "))
    seq2 = input("sequence second - ").split(" ")
    verify_len(n2, seq2)
    n3 = int(input("n3 -- "))
    seq3 = input("sequence third - ").split(" ")
    verify_len(n3, seq3)

    result1 = lcs_recursive(seq1, seq2)
    result2 = lcs_recursive(result1, seq3)

    print("Seq - {} and its len = {}".format(", ".join(result2), len(result2)))
