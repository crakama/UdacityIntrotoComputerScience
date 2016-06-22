# Given the variable,

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# define a procedure, how_many_days,
# that takes as input a number
# representing a month, and returns
# the number of days in that month.


def how_many_days(month):
    return days_in_month[month - 1]


m = raw_input("Enter Months")
how_many_days(m)