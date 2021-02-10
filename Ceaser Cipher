def encrypt(T,n):
    E =''
    for i in T.upper():
        E = E + (chr(( ((ord(i) - 65) + n)%26) + 65))
    return E
def decrypt(E,n):
    D = ''
    for i in E.upper():
        D = D + (chr(( ((ord(i) - 65) - n)%26) + 65))
    return D
T = input("Enter Text = ")
n = int(input("Enter shift = "))
E = encrypt(T,n)
print("Encrypted text = ",E)
D = decrypt(E,n)
print("Decrypted text = ",D)

"""
Output:
Enter Text = ATTACJATONCEYZ
Enter shift = 4
Encrypted text =  EXXEGNEXSRGICD
Decrypted text =  ATTACJATONCEYZ
"""
