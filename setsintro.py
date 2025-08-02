#Converting a list to a set

sample_list = [1,1,2,2,3,3]

sample_set = set(sample_list)

print(sample_list)

# Show  that sets are not indexable
# print(sample_set[2])

# Check if an element exists in the set
if 4 in sample_set:
    print("yes")
else:
    print("no")

# Adding element to the set
myset = set([])
myset.add(3)
myset.add(3)
myset.add(2)
myset.add(1)

print(myset)

# Remove the elements from the set,


myset.remove(2)
# Throws error if element is not present
myset.remove(5)
# Does not throw error if element is not present
myset.discard(5)


print(myset)


#Set operations
# 1) Union
# 2) Intersection
# 3) Difference
# 4) Symmetric difference

"""
A = {1,2,3,4,5}
B = [4,5,6,7,8]

Union means addition of sets

a U b = {1,2,3,4,5,6,7,8}


Intersection means the common elements between two sets 

a internsection B = {4,5}

c = {1,2,3}
d = {4,5,6}

c intersection D = None



difference of A and B is the elements  that exsist in A but not in B

a = {1,2,3,4,5,}
b = {4,5,6,7,8}
a - b = {1,2,3}
b - a = {6,7,8}

symmetric diference is (union of sets = intersection of sets)

a = {1,2,3,4,5}
b = {4,5,6,7,8}

a symDiff b = {1,2,3,6,7,8}
"""

a = {1,2,3,4,5}
b = {4,5,6,7,8}
