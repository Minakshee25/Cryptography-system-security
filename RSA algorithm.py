import math
choice = int(input("RSA Algorithm\nSelect type of plain text\n1. Numeric \n2. String\n"))
PT = input("Enter plain text = ")
p,q = map(int,input("Enter p and q = ").split(' '))
if(math.gcd(p,q) != 1):
    print("GCD of p and q should be 1!")
else:
    n = p*q
    phiofn = (p-1)*(q-1)
    for i in range(2,phiofn+1):
        if(math.gcd(i,phiofn) == 1):
            e = i
            break
    for i in range(100):
        if(((phiofn*i +1) % e) == 0):
            d = ((phiofn * i) + 1)//e
            break
    print("public key = ({0},{1})".format(e,n))
    print("private key = ({0},{1})".format(d,n))
    if (choice==1):
        CT = (int(PT)**e) % n
        print("Cipher text = ",CT)
        PT = (CT**d) % n
        print("Decrypted text = ",PT)
    else:
        CTlst = []
        DTlst = []
        lst = [ord(x) for x in PT]
        for i in lst:
            CTlst.append((i**e)%n)
        print("Cipher Text = ",''.join(map(str,CTlst)))
        for i in CTlst:
            DTlst.append((i**d)%n)
        DT = ''.join([chr(x) for x in DTlst])
        print("Decrypted text = ",DT)
        
"""
OUTPUT:

RSA Algorithm
Select type of plain text
1. Numeric 
2. String
1
Enter plain text = 5
Enter p and q = 7 17
public key = (5,119)
private key = (77,119)
Cipher text =  31
Decrypted text =  5


RSA Algorithm
Select type of plain text
1. Numeric 
2. String
2
Enter plain text = INDIA
Enter p and q = 7 17
public key = (5,119)
private key = (77,119)
Cipher Text =  8257178246
Decrypted text =  INDIA
"""
