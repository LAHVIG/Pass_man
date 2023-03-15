def inverseMod(a, m):
    for i in range(1,m):
        if ( m*i + 1) % a == 0:
            return ( m*i + 1) // a
    return None


p = 160390912114499758109275030312460194685863931436864531742691
q = 460374952936305732755303497312183367004304494680683253666831
n = p * q
phin = ( p - 1 ) * ( q - 1 )
e = 3
c = 42520998500002830371143160015315408987611901827743543916784841788341290700592155615177101344968803529684891053563701059
d = inverseMod(e,phin)
m = pow( c, d ,n)
hexString = hex(m)[2:]
print (hexString)
bytes_object = bytes.fromhex(hexString)
ascii_string = bytes_object.decode("ASCII")
print (ascii_string)