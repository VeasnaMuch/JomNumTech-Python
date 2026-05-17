item_set_1 = {"2", "2", "3", 3, "hello"}
print(item_set_1)

item_set_2 = {"Honda", 100, True, 3}
print(item_set_2)


print(item_set_1.intersection(item_set_2)) # item_set_1 & item_set_2
print(item_set_1.union(item_set_2)) # item_set_1 | item_set_2

#init empty set to avaiable
objSet = set()
objSet.add(2)
objSet.add("hello")
print(objSet)

objSet.discard(2)
print(objSet)