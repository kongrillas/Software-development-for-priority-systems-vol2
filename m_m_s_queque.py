import math

l = float(input())
m = float(input())
s = int(input())
sum = 0
for i in range(s):
    sum = sum + 1 / math.factorial(i) * ((l / m) **i)

P0 = 1 / (sum + 1 / math.factorial(s) * ((l / m) ** s) * ((s * m) / (s * m - l)))
ro = l / (s * m)
Ls = ((l * m * (l / m) ** s) / (math.factorial(s - 1) * (s * m - l) ** 2)) * P0 + l / m
Ws = Ls / l
Lq = Ls - l / m
Wq = Lq / l

print('The mean number of items in the queue Lq is ' + str(Lq))
print('The mean number of items in the system Ls is ' + str(Ls))
print('The mean waiting time in the queue Wq is ' + str(Wq))
print('The mean waiting time in the system Ws is ' + str(Ws))
print('The possibility of having n customers in the system ro is ' + str(ro))