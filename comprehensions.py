#List comprehensions
lst = [i  for i in range(100) if i % 3 ==0]
print(lst)
#dictionry comprehension

dict = {i:f"item{i}" for i in range(5)}
print(dict)
dict1 = {value:key for key,value in dict.items() }
print(dict1)

#Set comprehensions
#It does not print repeatable value
st = {i for i in [2,4,5,3,3,4,5,3] if i % 2 == 0}
print(st)

#Generator comprehensions
#It only iterate only ones
evens = ( i for i in range(20) if i%4 == 0)
print(type(evens))
for even in evens:
    print(even,end=" ")

