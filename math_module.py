import math

x = 1
n = 4
k = 2
a = 2.5
b = 8.6
c = 3.4

result = math.ceil(c)  # round of to the highest number 3.4 = 4
result = math.floor(c)  # round of to the lowest number 3.4 = 3
result = math.comb(n, k)  # 6

# How math.comb() works
nFactorial = math.factorial(n)
kFactorial = math.factorial(k)
nkFactorial = math.factorial(n-k)

result = nFactorial / (nkFactorial * kFactorial)  # 6.0

# Binomial Coefficient - math.comb(n, k)
# formula: (n k) = n! / (k! * (n - k)!)
#
# n  =      n!
# k     -----------
#       (n-k)! k!
#
#    =   4x3x2x1
#       -----------
#        (2x1) (2x1)
#
#    =    24
#       ------
#         4
#
#    = 6

# for more math methods visit
# https://docs.python.org/3/library/math.html
