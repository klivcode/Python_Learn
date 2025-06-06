#set is a colection of non repetitive elements and well defined and unordered data/objects
#set is mutable
# a={1,2,3,4,5}
# print(type(a))
# print(a)
# print(a,type(a))
# #add
# a.add(6)

# #remove
# a.remove(6)

# #update
# a.update([55,87,89])
# print(a)
# most important and highly used in data science|| in backednd are given below
#union
a={1,2,3,4,5}
b={5,6,7,8,9}
print(a.union(b))

#intersection
print(a.intersection(b))

#difference
print(a.difference(b))

#symmetric difference
print(a.symmetric_difference(b))

#subset
print(a.issubset(b))

#superset
print(a.issuperset(b))

#disjoint
print(a.isdisjoint(b))

#frozenset
a=frozenset(a)
print(a)
print(type(a))

#this is not a empty set this is a empty dictionary
a={}
print(type(a))

#empty set
b=set()
print(type(b))