#  Hint:  You may not need all of these.  Remove the unused functions.
#more hints from readme
# A brute-force solution would involve two nested loops, yielding a quadratic-runtime solution. How can we use a hash table in order to implement a solution with a better runtime?
# Think about what we can store in the hash table in order to help us to solve this problem more efficiently.
# What if we store each weight in the input list as keys? What would be a useful thing to store as the value for each key?
# If we store each weight's list index as its value, we can then check to see if the hash table contains an entry for limit - weight. If it does, then we've found the two items whose weights sum up to the limit!
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    #need to find the highest two pairs that sum up to the limit
    #need to store each weight list index value and check to see if hash table contain limit - weight
    #need to loop through weight list 
    #start at 0
    index = 0
    for item in weights:
        
    #find the difference between limit - weight
        difference = limit - item
    #Retrive items that are at limit
        value = hash_table_retrieve(ht, difference)
        #check if it exists
        if value is not None:
            if value < index:
                return(index, value)
            else:
            
                return(index, value)
        #add to hash table
        hash_table_insert(ht, item, index)        
        #increment index
        index = index + 1
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")


weights = [ 4, 6, 10, 15, 16 ]

print(get_indices_of_item_weights(weights,5,21))