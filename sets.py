def union(A, B):
    return [x for x in A] + [x for x in B if x not in A]

def intersection(A, B):
    return [x for x in A if x in B]

def set_difference(A, B):
    return [x for x in A if x not in B]

def symmetric_difference(A, B):
    return [x for x in A if x not in B] + [x for x in B if x not in A]

def cartesian_product(A, B):
    return [(x, y) for x in A for y in B]

#A = [1, 2, 3, 4, 5]
#B = [1, 3, 5, 7, 9]

#print union(A, B)
#print intersection(A, B)
#print set_difference(A, B)
#print set_difference(B, A)
#print symmetric_difference(A, B)
#print cartesian_product(A, B)
