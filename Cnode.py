from math import factorial
def ncr(n, r):
   res = 1
   if r > n - r:
      r = n - r

   for i in range(r):
      res *= (n - i)
      res //= (i + 1)

   return res

def solve(n):
   c = ncr(2 * n, n)
   return c // (n + 1)

n = 3
print(solve(n))