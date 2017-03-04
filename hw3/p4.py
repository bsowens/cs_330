import random
import math
import operator
 
#Graph type 1

def create1(n):
    g = {}
    for i in range(0,n):
        for j in range(i+1,n):
            g[(i,j)] = random.uniform(0, 1)
    return g

#Graph type 2

def create2(n):
    g = {}
    x = [random.uniform(0,1) for x in range(n)]
    y = [random.uniform(0,1) for x in range(n)]
    
    for i in range(n):
        for j in range(i+1,n):
            
            tups = list(zip(x,y))
            dist = math.sqrt((tups[i][0] - tups[j][0])**2 + (tups[i][1] - tups[j][1])**2)
            g[(tups[i],tups[j])] = dist
    return g


parent = dict()
rank = dict()

#Helper functions for union-find implementation

def find(vert):
    if parent[vert] != vert:
        parent[vert] = find(parent[vert])
    return parent[vert]

def union(vert1, vert2):
    r = find(vert1)
    q = find(vert2)
    if r != q:
        if rank[r] > rank[q]:
            parent[q] = r
        else:
            parent[r] = q
            if rank[r] == rank[q]: rank[q] += 1



def make(vert):
    #SImple tree making function
    parent[vert] = vert
    rank[vert] = 0


def krustykrab(graph):
    #Implementation of Kruskal's algorithm for finding an MST
    V = sorted(graph.items(), key=operator.itemgetter(1))
    verts = []
    mst = set()
    for i in range(len(V)):
        verts.append(V[i][0][0])
        verts.append(V[i][0][1])
    for vert in verts:
        make(vert)
    edges = list(graph.keys())

    for edge in V:

        vertys,myWeight = edge
        
        u,v = vertys

        if find(u) != find(v):
            union(u,v)
            mst.add(edge)

    return mst

#Test the algorithm on a random tree and return the average weight

def test1(n):
    avgs = []
    for x in range(5):
        g = create1(n)
        myMst = krustykrab(g)
        mstList = list(myMst)
        mySum = 0
        for i in range(len(mstList)):
            mySum += mstList[i][1]
        avgs.append(mySum)
    #print("Average over 5 tests", avgs)
    return sum(avgs)/5

def test2(n):
    avgs = []
    for x in range(5):
        g = create2(n)
        myMst = krustykrab(g)
        mstList = list(myMst)
        mySum = 0
        for i in range(len(mstList)):
            mySum += mstList[i][1]
        avgs.append(mySum)
    #print("Average over 5 tests", avgs)
    return sum(avgs)/5
        
#Find the average weight for each n [16,...,4096] 

def testAll1():
    results = []
    for n in [16,32,64,128,256]:#,512,1024,2048,4096]:
        results.append(test1(n))
    return results

def testAll2():
    results = []
    for n in [16,32,64,128,256,512,1024,2048,4096]:
        results.append(test2(n))
        print(results)
    return results

    
    
