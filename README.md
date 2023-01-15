# RSA Encryption

## Implementation

###### Step 1: choosing two large prime numbers, for the supplied example, they are between 100 and 1,000
###### Step 2: find N, such that N = p * q
###### Step 3: find T, such that T = (p - 1) * (q - 1)
###### Step 4: find e, d, such that (e * d) mod T = 1
###### Step 5: change text to ascci, and use ascii to the power of e mod N to encrypt the text
###### Step 6: use ecrypted ascii to the power of d mod N to decrypt the text