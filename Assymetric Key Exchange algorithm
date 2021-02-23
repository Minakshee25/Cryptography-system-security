q = int(input("Enter prime number q = "))
alpha =  int(input("Enter generator alpha = "))
XA = int(input("Enter public key of A = "))
XB = int(input("Enter public key of B = "))
YA = (alpha**XA) % q
YB = (alpha**XB) % q
KA = (YB**XA) % q
KB = (YA**XB) % q
print("Secret Key = ",KA)

"""
OUTPUT:
Enter prime number q = 11
Enter generator alpha = 2
Enter public key of A = 6
Enter public key of B = 8
Secret Key =  3
"""
