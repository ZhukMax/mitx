###########################
# 6.00.2x Problem Set 1: Space Cows

from pset1.ps1_partition import get_partitions
import time


# ================================
# Part A: Transporting Space Cows
# ================================
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows, limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    items_copy = sorted(cows.items(), key=lambda kv: kv[1], reverse=True)
    result = []

    while items_copy:
        indexes, tmp = [], []
        total_cost = 0.0
        for i in range(len(items_copy)):
            if (total_cost + items_copy[i][1]) <= limit:
                tmp.append(items_copy[i][0])
                # indexes.append(i)
                total_cost += items_copy[i][1]

        result.append(tmp)
        new_copy = []
        for i in range(len(items_copy)):
            if items_copy[i][0] not in tmp:
                new_copy.append(items_copy[i])

        items_copy = new_copy

    return result


# Problem 2
def brute_force_cow_transport(cows, limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    if cows == [] or limit == 0:
        return []

    result = []
    best_amount = 0
    for variant in get_partitions(cows.keys()):
        is_good = 1
        for part in variant:
            amount = 0
            for i in part:
                amount += cows[i]

            if amount > limit:
                is_good = 0

        if is_good == 1:
            if best_amount == 0 or best_amount > len(variant):
                best_amount = len(variant)
                result = variant

    return result

        
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    cows = load_cows("ps1_cow_data.txt")
    limit = 10
    print(cows)

    start = time.time()
    print(greedy_cow_transport(cows, limit))
    end = time.time()
    print(end - start)

    start = time.time()
    print(brute_force_cow_transport(cows, limit))
    end = time.time()
    print(end - start)

    pass


compare_cow_transport_algorithms()
