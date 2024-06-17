a='1101'
b='1111'
c='1011'
bina=int(a)
binb=int(b)
binc=int(c)
if bina>binb and bina>binc:
    print("Greatest is a")
elif binb>bina and binb>binc:
    print("greatest is b")
else:
    print('Graetest is c')
