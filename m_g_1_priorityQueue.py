K = int(input())
l = []
m = []
L = []
T = []
W = []
ro = []
R = []

for i in range(K):
    l.append(float(input()))
    m.append(float(input()))
for i in range(K):
        ro.append(l[i]/m[i])
        R.append(l[i] * (1 / m[i]) ** 2)
Rm = sum(R)*(1/2)
for i in range(1,K+1):
    tmp = 1
    for j in range(1,i+1):
        if j == i:
            tmp2 = tmp - ro[j-1]
        else:
            tmp = tmp - ro[j-1]

    W.append(Rm/(tmp*tmp2))
for i in range(K):
    L.append(l[i]*W[i])
    T.append(W[i] + 1/m[i])

for i in range(K):
    print('The possibility of having n customers in the system ro is ' + str(ro[i]))
    print('The mean number of items in the queue L for class ' + str(i+1) + " is " + str(L[i]))
    print("The mean waiting time W for class " + str(i+1) + " is " + str(W[i]))
    print("The total time in the system T for class " + str(i+1) + " is " + str(T[i]))

print('The mean residual service time R for all classes ' + str(Rm))




