import sys

def gcd(a, b):
	while b != 0:
		a, b = b, a%b
	return a

def lcm(a, b, gcd):
	return (a*b)//gcd

A, B = map(int, sys.stdin.readline().split())

gcd_val = gcd(A, B)
lcm_val = lcm(A, B, gcd_val)

sys.stdout.write(f"{gcd_val}\n{lcm_val}")


import sys
import math
# 입력 받기
A, B = map(int, sys.stdin.readline().split())
# 최대 공약수(GCD) 구하기
gcd = math.gcd(A, B)
# 최소 공배수(LCM) 구하기
lcm = (A * B) // gcd

sys.stdout.write(f"{gcd}\n{lcm}\n")