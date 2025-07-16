# Define two sets
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Set operations in action
union_set = A.union(B)   # The union (A | B) combines all unique
intersection_set = A.intersection(B)   #  the finds shared elements
difference_set = B.difference(A)      # Find elements in A but not in B

print("Set A:", A)
print("Set B:", B)
print("Union:", union_set)
print("Intersection:", intersection_set)
print("Difference (A - B):", difference_set)