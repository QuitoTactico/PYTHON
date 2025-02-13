set_a = {1, 2, 3}
set_b = {3, 4, 5}

# Union
union_result = set_a | set_b  # or use set_a.union(set_b)
print(union_result)  # Output: {1, 2, 3, 4, 5}

# Intersection
intersection_result = set_a & set_b  # or use set_a.intersection(set_b)
print(intersection_result)  # Output: {3}

# Difference
difference_result = set_a - set_b  # or use set_a.difference(set_b)
print(difference_result)  # Output: {1, 2}

# Symmetric Difference
symmetric_difference_result = set_a ^ set_b  # or use set_a.symmetric_difference(set_b)
print(symmetric_difference_result)  # Output: {1, 2, 4, 5}