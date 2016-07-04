# Creating an Empty Hash Table
# Define a procedure, make_hashtable,
# that takes as input a number, nbuckets,
# and returns an empty hash table with
# nbuckets empty buckets.

def make_hashtable(nbuckets):
	i = 0
    table = []
    while i < nbuckets:
        table.append([]) # everytime you go through the loop add one empty bucket to the hashtable
        i = i + 1 # increase i to keep from looping forever
    return table
print make_hashtable(3)