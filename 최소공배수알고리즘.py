def gcd(a, b):
  r = 0
  while b!=0:
    r = a%b
    a, b = b, r
  return a

def lcm(a, b):
  return (a * b) / gcd(a, b)


print(lcm(648, 231))

# a,b의 최소공배수는 a,b의 곳을 a,b의 최대공약수로 나눈 값과 같다.