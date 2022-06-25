""" OTP Generation (b)

	How to run:
		python 2_b.py [arg1] [arg2]

	Command line arguments (optional):
		[arg1] - Number of times to execute
        [arg2] - No. of digits in random number

	@author Samarth Saxena
"""

import gmpy2, time, sys
from gmpy2 import mpz

r = gmpy2.random_state()

def main():
	n=1
	digits = 1023

	if len(sys.argv)>1:
		n = int(sys.argv[1])
	if len(sys.argv)>2:
		digits = int(sys.argv[2])

	start = time.time()

	min = pow(10,digits-1)
	max = pow(10,digits)-min-1

	seed = gmpy2.mpz_random(r,max)+min

	print(seed)
	snum = str(seed)
		
		# x = -1
	for i in range(n):

		for j in range(6):
			x = gmpy2.mpz_random(r,digits)
			# if(x>=digits):
			# 	x = 0
			while(j==0 and snum[x]=='0'):
				x= x+1
				if(x>=digits):
					x = 0
			print(snum[x], end=" ")
			x = x+1
		print()

	end = time.time()
	print("\n(%fs)" %(end-start))


if __name__=="__main__":
	main()