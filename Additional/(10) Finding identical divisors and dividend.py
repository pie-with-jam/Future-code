#

n = int(input())
m = int(input())

result = (n % m == 0) or (m % n == 0)

print(int(result))