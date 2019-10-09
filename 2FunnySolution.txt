string=input("Enter a String ")
list1 = []
list12 = []

list2 = []
list22 = []

for i in string:
    a = ord(i)
    list1.append(a)

list12 = list1

print(list1)
rev = string[-1::-1]
print(rev)

for i in rev:
    a = ord(i)
    list2.append(a)
    
print(list2)

list22 = list2

result = []
result1 = []
for i in range(1,len(list12)):
    if(list12[i]>list12[i-1]):
        diff = list12[i]-list12[i-1]
    else:
        diff = list12[i-1] - list12[i]
    result.append(diff)

print(result)

for i in range(1,len(list22)):
    if(list22[i]>list22[i-1]):
        diff = list22[i]-list22[i-1]
    else:
        diff = list22[i-1] - list22[i]
    result1.append(diff)

print(result1)

if result == result1:
    print("Funny")
else:
    print("Not Funny")
