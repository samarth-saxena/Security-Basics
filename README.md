# Security Basics
A series of programs that I wrote as a part of the course Foundations of Computer Security. 

## 1. Password generator
Given a plain text string as input, the program converts it into some password-ready strings.  
Eg: `Helloworld -> #3l10W0R1)`

To run:
```
python 1-password_generator.py [arg1]
```
- `arg1`: Number of passwords to be generated  


## 2. OTP Generation
A program to generate a random number of 1023 digits and extract a 6 digit OTP from it.
- 2a utilises the `random` library
- 2b utilises the `gmpy2` library
The former runs faster, and generates better random numbers.

To run:
```
python 2a-otp_generation.py [arg1] [arg2]
```
- `arg1`: Number of times to execute
- `arg2`: No. of digits in random number  


## 3. Diffie Helman Key Exchange Algorithm
This program implements the Diffie Helman algorithm, and demonstrates a secure key exchange between Alice and Bob. It utilises the `gmpy2` library for random number generation.

To run:
```
python 3-dh_key_exchange.py [arg1] [arg2] [arg3]
```
- `arg1`: Number of times to execute
- `arg2`: No. of digits in public key
- `arg3`: No. of digits in private key


## 4. RSA Encryption
This program implements the RSA encryption algorithm, utilising `gmpy2` for generating the public keys. The working is demonstrated by taking a user input, encrypting it and subsequently decrypting it.

To run:
```
python 3-dh_key_exchange.py [arg1] [arg2]
```
- `arg1`: Number of times to execute
- `arg2`: No. of digits in p and q