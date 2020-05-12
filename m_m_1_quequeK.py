l = float(input())
m = float(input())
K = int(input())
ro = l/m
if (l==m):
    PO = 1/(K+1)
else:
    PO = (1-ro)/(1-ro**(K+1))
PK = PO * ro**K
Ls = ro/(1-ro)-((K+1)*ro**(K+1))/(l-ro**(K+1))
Lq = Ls-ro**(1-PK)
Ws = Ls/(l*(1-PK))
Wq = Ws-1/m
print('The mean number of items in the queue Lq is ' + str(Lq))
print('The mean number of items in the system Ls is ' + str(Ls))
print('The mean waiting time in the queue Wq is ' + str(Wq))
print('The mean waiting time in the system Ws is ' + str(Ws))
print('The possibility of having n customers in the system ro is ' + str(ro))