# Define a procedure, replace_spy,
# that takes as its input a list of
# three numbers, and modifies the
# value of the third element in the
# input list to be one more than its
# previous value.

spy = [0,0,7]

def replace_spy(p): # this takes one parameter as its input, called p
    p[2] = p[2] + 1


replace_spy(spy)
print spy
#>>> [0,0,8]

# Define a procedure, sum_list,
# that takes as its input a
# list of numbers, and returns
# the sum of all the elements in
# the input list.











def sum_list(p):
    result = 0
    for e in p:
        result = result + e
    return result
print sum_list([1, 4, 7])