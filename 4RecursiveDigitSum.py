n = int(input("Enter the no."))

if n<=1:
    print("Enter number in range between 1 and 10500000 ")
if n>=10500000:
    print("Enter number in range between 1 and 10500000 ")

n = str(n)

k = int(input("Enter the no. of concatenations "))
if k<=1:
    print("Enter number in range between 1 and 105 ")
if k>=105:
    print("Enter number in range between 1 and 105 ")

a=n*k
print(a)


sum1 = 0
for i in a:
    sum1 = sum1 + int(i)

print(sum1)

sum1 = str(sum1)
total = 0
if int(sum1)>9:
    for i in sum1:
        total = total + int(i)
        

print(total)
    

