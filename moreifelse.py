# Define a procedure, is_friend, that takes
# a string as its input, and returns a
# Boolean indicating if the input string
# is the name of a friend. Assume
# I am friends with everyone whose name
# starts with either 'D' or 'N', but no one
# else. You do not need to check for
# lower case 'd' or 'n

def is_friend(string):
	if string[0] == 'D' or string[0] == 'N':
		return True
	return False
