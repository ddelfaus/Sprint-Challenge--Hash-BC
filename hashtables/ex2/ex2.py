#  Hint:  You may not need all of these.  Remove the unused functions.
# more hints

#The crux of this problem requires us to 'link' tickets together to reconstruct the entire trip. 
# For example, if we have a ticket ('SJC', 'BOS') that has us flying from San Jose to Boston, 
# then there exists another ticket where Boston is the starting location, ('BOS', 'JFK').

# We can hash each ticket such that the starting location is the key and the destination is the value. 
# Then, when constructing the entire route, 
# the ith location in the route can be found by checking the hash table for the i-1th location.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    #need to store all tickets from list

    for item in tickets:
        hash_table_insert(hashtable, item.source, item.destination)
        #check for the ticket that has none as its starting point or source
        if item.source == "NONE":
            route[0] = item.destination
    #need a starting point
    index = 0
    #need a current location
    current = 0
    #going to loop through until destination is none since that will be the end of the trip
    while True:
        current = route[index]
        next_airport = hash_table_retrieve(hashtable, current)

        index = index + 1
        route[index] = next_airport
        if next_airport == "NONE":
            route.pop()
            break
           
    return route

 

