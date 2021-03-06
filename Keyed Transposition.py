import math
def Encrypt(PT,K):
    n = math.ceil(len(PT) / len(K))
    PTlst = []
    for i in range(n):
        PTlst.append(PT[i*len(K) : (i*len(K) + len(K))])
    E = ''
    dctlist = []
    for i in PTlst:
        dct = dict(zip(i,K))
        dct = {k: v for k, v in sorted(dct.items(), key=lambda dct: dct[1])}
        dctlist.append(dct)
        E = E + ''.join(dct.keys())
    return E,dctlist
def Decrypt(E,dctlist,K):
    D = ''
    for i in dctlist:
        for j in K:
            if(j in i.values()):
                D = D + list(i.keys())[list(i.values()).index(j)]
    return D
PT = list(input("KEYED TRANSPOSITION \nEnter plain text = "))
K = list(map(int,input("Enter key = ")))
E,dctlist = Encrypt(PT,K)
print("Encrypted text = ", E)
D = Decrypt(E,dctlist,K)
print("Decrypted text = ",D)

"""
Output:
KEYED TRANSPOSITION 
Enter plain text = sixfourfive
Enter key = 2401
Encrypted text =  xfsirfoueiv
Decrypted text =  sixfourfive
"""
