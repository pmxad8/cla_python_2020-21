a = int(input("Enter your first number:")) 

b = int(input("Enter your second number:"))



x = 1



while (a/pow(2.0,x)).is_integer() and (a/pow(2.0,x))<a and (b/pow(2.0,x)).is_integer() and (b/pow(2.0,x))<b: 

    x=x+1.0



print ("The highest common power of 2 is:")

print (x)
print(2**x)

