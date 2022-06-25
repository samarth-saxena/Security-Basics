""" Strong Password Generation

	How to run:
		python 1.py [arg1]

	Command line arguments:
		[arg1] - Number of passwords to be generated

	@author Samarth Saxena
		
"""

import gmpy2, sys
from gmpy2 import mpz

def main():
	r = gmpy2.random_state()
	n = 1

	if len(sys.argv)>1:
		n  = int(sys.argv[1])

	text = input()
	arr = [
		['a', 'A', '@', '4'],
		['b', 'B', '8', '6'],
		['c', 'C', '(', '<'],
		['d', 'D', ")"],
		['e', 'E', '3'],
		['f', 'F'],
		['g', 'G', '9'],
		['h', 'H', '#'],
		['i', 'I', '1', '!'],
		['j', 'J'],
		['k', 'K'],
		['l', 'L', '1', '|'],
		['m', 'M'],
		['n', 'N'],
		['o', 'O', '0'],
		['p', 'P', '?'],
		['q', 'Q'],
		['r', 'R'],
		['s', 'S', '$', '5'],
		['t', 'T', '+'],
		['u', 'U'],
		['v', 'V'],
		['w', 'W'],
		['x', 'X'],
		['y', 'Y'],
		['z', 'Z', '2']
	]

	text = text.lower()

	for i in range(n):
		textList = list(text)
		# print(text)
		for i,x in enumerate(textList):
			if x.isalpha() :
				# print(x)
				# print(ord(x))
				num = ord(x)-97
				textList[i]=arr[num][gmpy2.mpz_random(r,len(arr[num]))]
		password = "".join(textList)
		print(password)

if __name__=="__main__":
	main()