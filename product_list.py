# Define a procedure, product_list,
# takes as input a list of numbers,
# and returns a number that is
# the result of multiplying all
# those numbers together.


def product_list(lst):
    mult = 1

    for i in lst:
        mult = mult * i
    print mult

num = [1, 2, 3, 4]
product_list(num)


