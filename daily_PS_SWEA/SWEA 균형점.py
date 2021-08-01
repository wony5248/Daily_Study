TC = int(input())

for i in range(1, TC+1):
    corx = []
    mass = []
    N = int(input())
    x = list(map(float, input().split()))
    for j in range(len(x)//2):
        corx.append(x[j])
    for j in range(len(x)//2, len(x)):
        mass.append(x[j])
    result = []
    for j in range(1, N):
        lcorx = corx[j-1]
        rcorx = corx[j]
        while rcorx - lcorx > 1 / (10**12):
            mid = (lcorx + rcorx) / 2
            lmass = 0
            rmass = 0
            for k in range(N):
                F = mass[k] / ((mid-corx[k])**2)
                if corx[k] < mid:
                    lmass += F
                else:
                    rmass += F
            if lmass < rmass:
                rcorx = mid
            else:
                lcorx = mid
        result.append(mid)
    print("#%d" %i, end=" ")
    for j in range(N-1):
        print("%.10f" % result[j], end=" ")
    print()
