dict1 = {1:'one',2:'two',3:'three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine',10:'Ten',
         11:'Eleven',12:'Twelve',13:'Thirteen',14:'Fourteen',15:'Fifeteen',16:'Sixteen',17:'Seventeen',18:'Eighteen',19:"Nineteen",
         20:"Twenty",21:"Twenty One ",22:"Twenty Two ",23:"Twenty Three",24:"Twenty four",25:"Twenty five",26:"Twenty six",27:"Twenty Seven",
         28:"Twenty Eight ",29:"Twenty  Nine",
         30:"Thirty",
         40:'Forty',
         50:'Fifty'}


hour = int(input("Enter time in hours :"))
minutes = int(input("Enter time in minutes: "))

val = dict1[hour]
print(val)

if (minutes == 0):
    print(str(hour)+" o' clock ")    
elif(minutes<30):
    print(str(minutes)+" minutes past "+str(hour))
elif(minutes>30):
    print(str(60 - minutes)+" minutes to "+str(hour))

