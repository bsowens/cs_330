S = ["A","A","B","A","A","A","A","A","A","B","A","A","A","A","B"]


extra = S[0]
S = S[1:]
n = len(S)
S1 = S[0:n//2]
S2 = S[n//2 + 1:]
newSet = []
for i in range(len(S)//2 ):
    print("S1 = ",S1)
    print("S2 = ",S2)
    if S1[i] == S2[i]:
        S2 = S2[i+1:]
    if S1[i] != S2[i]:
        if S1[i] == extra:
            S2 = S2[i+1:]
        if S2[i] == extra:
            S1 = S1[i+1:]

