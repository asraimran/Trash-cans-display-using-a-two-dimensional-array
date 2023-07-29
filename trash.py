def getposint(prompt):
    while prompt<=0:
        print("Invalid input ")
        prompt=int(input("enter again"))
    return prompt
def getboundedint(prompt,lower,upper):
    prompt="invalid input"
    while lower<=0:
        print(prompt)
        lower=int(input("enter lower value again:"))
    while upper<=0:
        print(prompt)
        upper=int(input("enter upper value again:"))
    return prompt,upper,lower
def displaytrashcan(t,j):
    b=[]
    p=[]
    c=0
    for i in range(0,t):
        b.append(c)
    for k in range(0,j):
        p.append(b)
    return p
def trashcan(t,a):
    lst = [] 
    for i in range(a):
        lst.append([0]) 
        for j in range(t-1): 
            lst[i].append(0)
    return lst
def getboundedint(prompt,lower,upper):
    lower=0
    while prompt<0 or prompt>upper:
        print("invalid input try again:")
        prompt=int(input("enter in which you want to enter bag:"))
    return prompt
def addtrash(a,k,m):
    i=0
    m=m-1
    while i<=m:
        if k[i][a]==0:
            k[i][a]=1
            break
        elif k[i][a]==k[m][a]:
            print("One can fill . Time to have trash picked up")
            break
        else:
            i+=1
    return k
        