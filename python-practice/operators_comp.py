a = 10
b = 3
c = 3

if(a==b):
    print("A is equal to B", "\nValue of A", a, "\nValue of B ", b)
else:
    print("A is not equal to B", "\nValue of A", a, "\nValue of B", b)



print ("\n Comparing b and C values where a =",a, "b = ",b, "c =",c)

if(b==c & c <a):
    print("B and C is equal and also  c is less than a")

else:
    print("\nB and C is not equal")



d = a<<b
print("Binary Left shift example ", d)


d= a>>b
print ("Value of Binary Right Shift", d)

