cet = {"rohit", "mohsin", "muntazir", "SNeha"}
jee = {"rohit", "mohsin", "muntazir", "Sania"}
neet = {"ruhi", "Rita", "muntazir", "basharat"}

# Function to show union
def show_union(a, b, c):
    print("Students appearing for CET, JEE or NEET:")
    print(set.union(a, b, c))

# Function to show intersection
def show_intersection(a, b, c):
    print("Students present in CET, JEE and NEET:")
    print(set.intersection(a, b, c))

# Function to show difference
def show_difference(a, b):
    print(" present in CET but not in JEE:")
    print(set.difference(a, b))

def show_difference_jee_neet(b, c):
    print("Students present in JEE but not in NEET:")
    print(set.difference(b, c))

def show_difference_neet_cet(c, a):
    print("Students present in NEET but not in CET:")
    print(set.difference(c, a))

# Function to show symmetric difference
def show_symmetric_difference(a, b):
    print("Students present in CET or JEE but not both:")
    print(set.symmetric_difference(a, b))

# Call all functions
show_union(cet, jee, neet)
show_intersection(cet, jee, neet)
show_difference(cet, jee)
show_difference_jee_neet(jee, neet)
show_difference_neet_cet(neet, cet)
show_symmetric_difference(cet, jee)
