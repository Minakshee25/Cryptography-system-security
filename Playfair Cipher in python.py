def Encrypt(T,a):
    L =[T.upper()[i:i+2] for i in range(0, len(T)-1, 2)]
    if (len(T)%2 != 0):
        L.append(T.upper()[len(T)-1] + 'Z')
    E = ''
    for l in L:
        if (('I' in T.upper()) and ('J' in T.upper())):
            if (('I' in l[0]) or ('J' in l[0])):
                i1, j1 = np.where(a == 'IJ')
                i2, j2 = np.where(a == l[1])
            elif (('I' in l[1]) or ('J' in l[1])):
                i1, j1 = np.where(a == l[0])
                i2, j2 = np.where(a == 'IJ')
            else:
                i1, j1 = np.where(a == l[0])
                i2, j2 = np.where(a == l[1])
        else:
            i1, j1 = np.where(a == l[0])
            i2, j2 = np.where(a == l[1])
        if (j1[0]==j2[0]):
            E = E + a[(i1[0]+1)%5][j1[0]] + a[(i2[0]+1)%5][j1[0]]
        elif (i1[0] == i2[0]):
            E = E + a[i1[0]][(j1[0]+1)%5] + a[i1[0]][(j2[0]+1)%5]
        else:
            E = E + a[i1[0]][j2[0]] + a[i2[0]][j1[0]]
    return E
def Decrypt(T,a):
    L =[T.upper()[i:i+2] for i in range(0, len(T)-1, 2)]
    if (len(T)%2 != 0):
        L.append(T.upper()[len(T)-1] + 'Z')
    E = ''
    for l in L:
        if (('I' in T.upper()) and ('J' in T.upper())):
            if (('I' in l[0]) or ('J' in l[0])):
                i1, j1 = np.where(a == 'IJ')
                i2, j2 = np.where(a == l[1])
            elif (('I' in l[1]) or ('J' in l[1])):
                i1, j1 = np.where(a == l[0])
                i2, j2 = np.where(a == 'IJ')
            else:
                i1, j1 = np.where(a == l[0])
                i2, j2 = np.where(a == l[1])
        else:
            i1, j1 = np.where(a == l[0])
            i2, j2 = np.where(a == l[1])
        if (j1[0]==j2[0]):
            E = E + a[(i1[0]-1)%5][j1[0]] + a[(i2[0]-1)%5][j1[0]]
        elif (i1[0] == i2[0]):
            E = E + a[i1[0]][(j1[0]-1)%5] + a[i1[0]][(j2[0]-1)%5]
        else:
            E = E + a[i1[0]][j2[0]] + a[i2[0]][j1[0]]
    return E
T = input("PLAYFAIR CIPHER\nEnter Text = ")
K = input("Enter Key = ")

a = [i for i in K.upper()]
for i in range(65,91):
    if ((chr(i)=='I') and ('I' in T.upper()) and ('J' in T.upper())):
        a.append(chr(i) + chr(i+1))
    elif (chr(i) == 'J'):
        pass
    elif chr(i) not in K.upper():
        a.append(chr(i))
a = np.array(a)
a = a.reshape(5,5)
E = Encrypt(T,a)
print("Encrypted Text = ",E)
D = Decrypt(E,a)
print("Decrypted text = ",D)


"""
Output:
PLAYFAIR CIPHER
Enter Text = VIDYALAY
Enter Key = PAY
Encrypted Text =  UKFPYKYB
Decrypted text =  VIDYALAY
"""
