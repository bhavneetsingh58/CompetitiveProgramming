n = int(input("Enter the no. of questions "))

if n<=1:
    print("Enter number in range between 1 and 105 ")
if n>=105:
    print("Enter number in range between 1 and 105 ")

q = int(input("Enter the no. of queries "))
if q<=1:
    print("Enter number in range between 1 and 105 ")
if q>=105:
    print("Enter number in range between 1 and 105 ")


print("Enter the time slots ")
list1 = []
for t in range(n):
    a = int(input())
    list1.append(a)

print(list1)

print("Enter the scores of the queries ")
list2 = []
for t in range(n):
    a = int(input())
    list2.append(a)

print(list2)

k = int(input("Enter the no. of qustions to be solved "))
if (k<1):
    print("Enter number in range between 1 and "+str(n))
if (k>n):
    print("Enter number in range between 1 and "+str(n))

val = []
list12 = list2
for i in range(k):
    a = max(list12)
    value = list12.index(a)
    val.append(value)
    list12.insert(value+1,0)
    list12.remove(a)

#print(val)

print("The time slots for the queries of maximum scores ")
result = []
for i in val:
    result.append(list1[i])

print(result)

print("The sum of the time slots ")
print(sum(result))
    
