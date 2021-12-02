import enum
class Days(enum.Enum):
    Sun=1
    Mon=2
    Tue=3
    Wed=4
    Thu=5
    Fri=6
    Sat=7
print ("The enum member as a string : ", end="")
print (Days.Mon)

print("The enum member as a repr() is :", end="")
print(repr(Days.Mon))

print("The type of enum member is ", end="")
print (type(Days.Sun))

print ("The name of enum member is :", end="")
print(Days.Wed.name)

print ("Printing all members using for loop",end="\n")
for weekday in (Days):

    print(weekday.name," - ", weekday.value,"\n")

print ("\n", "That is all for the day")


