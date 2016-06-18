# Define a procedure, bigger, that takes in
# two numbers as inputs, and returns the
# greater of the two inputs.


# print bigger(2,7)
#>>> 7

# print bigger(3,2)
#>>> 3

# print bigger(3,3)
#>>> 3


def bigger(n, m):
    maxnum = max(n, m)
    return maxnum
n = 8
m = 9
bigger(n, m)