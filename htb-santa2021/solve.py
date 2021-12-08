import random
from math import gcd

mod = 256
a = []
for i in range(1, 256):
    if gcd(i, mod) == 1:
        a.append(i)


dt = open('encrypted.bin', 'wb')

print(a)  

# enc = (a*byte + b) %  mod 
# enc = x % mod 
