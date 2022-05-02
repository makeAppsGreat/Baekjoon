M, N = 100, 100; print(M, N)
T = list()

for i in range(M):
    T.append( list() )
    for _ in range(N): T[i].append(0)


T[0][0] = 1


for j in T: print(*j)

