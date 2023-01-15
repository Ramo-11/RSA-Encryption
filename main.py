import random
import time

from math import gcd as bltin_gcd

def modinv(e, T):
    a, b = T, e
    x, y = 0, 1
    while b:
        q, r = divmod(a, b)
        a, b, x, y = b, r, y, x - (q * y)
    if a != 1:
        raise Exception("Modular inverse does not exist")
    return x

def primesInRange(x, y):
    prime_list = []
    for n in range(x, y):
        isPrime = True

        for num in range(2, n):
            if n % num == 0:
                isPrime = False

        if isPrime:
            prime_list.append(n)
            
    return prime_list

def coprime(a, b):
    return bltin_gcd(a, b) == 1

def main():
    minPrime = 100
    maxPrime = 1000
    user_input = input("Input text to encrypt:\n")

    print("\nStep 1: choosing two large prime numbers, for this example, it will be between {} and {}".format(minPrime, maxPrime))
    prime_list = primesInRange(minPrime, maxPrime)
    p = random.choice(prime_list)
    q = p
    while q == p:
        q = random.choice(prime_list) 
    print("p = {}, q = {}".format(p, q))

    time.sleep(1)
    print("\nStep 2: find N, such that N = p * q")
    N = q*p
    print("N = {}".format(N))

    time.sleep(1)
    print("\nStep 3: find T, such that T = (p - 1) * (q - 1)")
    T = (p-1) * (q-1)
    print("T = {}".format(T))

    time.sleep(1)
    print("\nStep 4: find e, d, such that (e * d) mod T = 1")
    coprime_e_values = (potential_e for potential_e in range(0, T) if coprime(potential_e, T))
    e = random.choice(list(coprime_e_values))
    d = modinv(e, T)
    while d <= 0:
        d += T 
    print("e = {}, d = {}".format(e, d))
    print("To check, the result of ({} * {}) % {} = {}".format(e, d, T, (e * d) % T))

    time.sleep(1)
    print("\nStep 5: change text to ascci, and use ascii to the power of e mod N to encrypt the text")
    print("\nText before encryption:")
    ascii_string = [ord(c) for c in user_input]
    print("string: {}".format(user_input))
    print("ascii (combined): {}".format("".join(str(i) for i in ascii_string)))
    time.sleep(1)
    print("\nEncrypted text:")
    encrypted = [pow(num, e) % N for num in ascii_string]
    print("string: {}".format("".join(chr(i) for i in encrypted)))
    print("ascii (combined): {}".format("".join(str(i) for i in encrypted)))
    time.sleep(1)
    print("\nStep 6: use ecrypted ascii to the power of d mod N to decrypt the text")
    print("\ndecrypted text:")
    decrypted = [pow(num, d) % N for num in encrypted]
    print("string: {}".format("".join(chr(i) for i in decrypted)))
    print("ascii (combined): {}".format("".join(str(i) for i in decrypted)))

  
if __name__=="__main__":
    main()