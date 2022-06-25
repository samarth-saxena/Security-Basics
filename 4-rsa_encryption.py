""" RSA Encyption Algorithm

	How to run:
		python 3.py [arg1] [arg2]

	Command line arguments (optional):
		[arg1] - Number of times to execute
        [arg2] - No. of digits in p and q

	@author Samarth Saxena
"""

import gmpy2, time, sys
from gmpy2 import mpz

r = gmpy2.random_state()
digits = 1023
times=1
e = 65537

def encrypt(m, p, q):
	print("p: %d" %p)
	print("q: %d" %q)
	print("m: %d" %m)

	n = p*q
	phi = (p-1)*(q-1)
	d = gmpy2.invert(e,phi) 		# invert(x, m) returns y such that x * y == 1 modulo m
	c = pow(m,e,n)

	print("\nc: %d" %c)
	print("e: %d" %e)
	print("d: %d" %d)
	print("n: %d" %n)
	print("Encrypted\n")

	return c, d, n

def decrypt(c,d,n):
	m = pow(c,d,n)

	print("m: %s" %m)
	print("Decrypted")

	return m

def main():
	global digits
	global times

	if len(sys.argv)>1:
		times = int(sys.argv[1])
	if len(sys.argv)>2:
		digits = int(sys.argv[2])

	min = pow(10,digits-1)
	max = pow(10,digits)-min-1

	for i in range(times):
		p = gmpy2.next_prime(gmpy2.mpz_random(r,max)+min)
		q = gmpy2.next_prime(gmpy2.mpz_random(r,max)+min)

		#Not necessary, but for extreme cases
		while(gmpy2.gcd(e,p-1)!=1):
			p = gmpy2.next_prime(gmpy2.mpz_random(r,max)+min)
		while(gmpy2.gcd(e,q-1)!=1):
			q = gmpy2.next_prime(gmpy2.mpz_random(r,max)+min)

		# p = int(input("enter p: "))
		# q = int(input("enter q: "))
		m = int(input("enter m: "))

		# encrypt(m,p,q)
		# c = int(input("enter c: "))
		# d = int(input("enter d: "))
		# n = int(input("enter n: "))

		c,d,n = encrypt(m,p,q)
		dm = decrypt(c,d,n)


if __name__=="__main__":
	main()