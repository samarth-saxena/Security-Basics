""" Diffie Hellman Key Exchange

	How to run:
		python 3.py [arg1] [arg2] [arg3]

	Command line arguments (optional):
		[arg1] - Number of times to execute
		[arg2] - No. of digits in public key
		[arg3] - No. of digits in private key

	@author Samarth Saxena
"""

import sys
import gmpy2
from gmpy2 import mpz

r = gmpy2.random_state()
prv_digits = 1000
pub_digits = 1023
n = 1

def alice_sends_bob(p,g):

	min = pow(10,prv_digits-1)
	max = pow(10,prv_digits)-min-1

	a = gmpy2.mpz_random(r,max)+min

	# a = 4
	A = pow(g,a,p)
	print("(Alice)")
	print("Private key: %d" %(a))
	print("Public key: %d\n" %(A))
	return a, A

def bob_sends_alice(p,g):

	min = pow(10,prv_digits-1)
	max = pow(10,prv_digits)-min-1

	b = gmpy2.mpz_random(r,max)+min

	# b = 3
	B = pow(g,b,p)
	print("(Bob)")
	print("Private key: %d" %(b))
	print("Public key: %d\n" %(B))
	return b, B

def print_shared_secret_alice(B, a, p):
	SA = pow(B,a,p)
	print("Shared key (Alice): %d" %(SA))

def print_shared_secret_bob(A,b,p):
	SB = pow(A,b,p)
	print("Shared key (Bob): %d\n" %(SB))


def main():
	global n
	global prv_digits
	global pub_digits
	
	if len(sys.argv)>1:
		n = int(sys.argv[1])
		pub_digits = int(sys.argv[2])
		prv_digits = int(sys.argv[3])

	# Max, min of random number
	min = pow(10,pub_digits-1)
	max = pow(10,pub_digits)-min-1

	for i in range(n):
		# p = gmpy2.next_prime(gmpy2.mpz_random(r,max)+min)
		# g = gmpy2.mpz_random(r,max)+min

		p = int(input("enter p: "))
		g = int(input("enter g: "))

		print("\np: %d" %(p))
		print("g: %d\n" %(g))

		a, A = alice_sends_bob(p,g)
		b, B = bob_sends_alice(p,g)
		print_shared_secret_alice(B,a,p)
		print_shared_secret_bob(A,b,p)

		print("---\n")


if __name__=="__main__":
	main()