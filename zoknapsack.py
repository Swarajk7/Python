from math import ceil
def knapsack(items, maxweight):
    bestvalues = [[0] * (maxweight + 1)
                  for i in xrange(len(items) + 1)]

    for i, (value, weight) in enumerate(items):
        i += 1
        for capacity in xrange(maxweight + 1):
            if weight > capacity:
                bestvalues[i][capacity] = bestvalues[i - 1][capacity]
            else:
                candidate1 = bestvalues[i - 1][capacity]
                candidate2 = bestvalues[i - 1][capacity - weight] + value
                bestvalues[i][capacity] = max(candidate1, candidate2)
    reconstruction = []
    i = len(items)
    j = maxweight
    while i > 0:
        if bestvalues[i][j] != bestvalues[i - 1][j]:
            reconstruction.append(i - 1)
            j -= items[i - 1][1]
        i -= 1
    reconstruction.reverse()
    return bestvalues[len(items)][maxweight], reconstruction

arr=['FIASCO',1,2,3,4,5,6,7,8,9,10,'OUT OF BOX']

if __name__=='__main__':
        c=int(input())
        for xx in range(c):
            N,W=raw_input().split()
            N=int(N)
            W=int(W)
            w=[]
            r=[]
            for xxx in range(N):
                a=map(int,raw_input().split())
                w.append((a[0],a[2]))
                r.append(a[1])
            ans=knapsack(w,W)
            #print ans
            tr=0
            cnt=0
            #print ans,v,w,W
            for i in ans[1]:
                tr+=r[i]
                cnt+=1
            tr=tr/cnt
            tr=tr/10
            if tr==0:
                    print arr[0]
                    continue
            tr+=1
            if tr==11:
                    print arr[-1]
            else:
                    print tr
            
