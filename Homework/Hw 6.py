from functools import reduce

#Basic Lambda 
(lambda x: print("Even")if x%2==0 else print("odd"))(8)
#output=Even


#advanced

sum_list=lambda lst:sum(lst)

print (sum_list([2,4,5,6,67,6,5,4]))
#output=99




#sorting with lamda
names=["Marvin","Matt","preston","Richard"]
names_sorted=sorted(names, key=lambda name: name[1])
print(names_sorted)
#output=['Marvin', 'Matt', 'Richard', 'preston']



#map with lambda
numbers=[1,2,3,4,5,6,7,8,9]
square=list(map(lambda x: x** 2, numbers))
print(square)
#output=[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#filtering with lambda
even=list(filter(lambda x: x%2==0,numbers))
print(even)
#output=[2, 4, 6, 8, 10]

#reducing with lambda
product = reduce(lambda x,y: x*y, numbers)
print(product)
#output=3628800

#enumerating
strings=["apple","orange","pear","banana"]
b=enumerate(strings, start=1)
print(list(b))
#output=[(1, 'apple'), (2, 'orange'), (3, 'pear'), (4, 'banana')]

#zip()
ages=[17,18,19,25]
zipped=list(zip(names,ages))
print(zipped)
#output=[('Marvin', 17), ('Matt', 18), ('preston', 19), ('Richard', 25)]
