def merge_sorted_lists(list1, list2):
    # i know there's a better solution, iterating in both lists, but naaah... this is a course
    list1.extend(list2)
    return sorted(list1)