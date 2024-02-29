a = {1,2,3,3,4,4,5}
print(a)
b = {4,5,6,7,8}
print(a | b)
print(a.union(b))

print(a & b)
print(a.intersection(b))

print(a.difference(b)) # a - b
print(b -a )

print(a ^ b)
print("--------------")
a.add("abc")
a.update([1,2,9,12,19], range(19,30))
print(a)
a.discard("abc")
print(a)