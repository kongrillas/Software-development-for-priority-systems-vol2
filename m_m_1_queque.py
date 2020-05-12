l = float(input())
m = float(input())
ro = l/m
Ls = ro/(l-ro)
Lq = (ro**2)/ (l-ro)
Wq = Lq/l
Ws = Ls/l
print('The mean number of items in the queue Lq is ' + str(Lq))
print('The mean number of items in the system Ls is ' + str(Ls))
print('The mean waiting time in the queue Wq is ' + str(Wq))
print('The mean waiting time in the system Ws is ' + str(Ws))
print('The possibility of having n customers in the system ro is ' + str(ro))