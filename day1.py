
f=open("input.txt","r")
l1=[]
l2=[]
l=f.readlines()
for i in l:
    l1.append(list(map(int,i.split(" "*3)))[0])
    l2.append(list(map(int,i.split(" "*3)))[1])
def distance(l1,l2):
    s=0
    l1.sort()
    l2.sort()
    for i in range(min(len(l1),len(l2))):
        s+=abs(l1[i]-l2[i])
    return s
print(distance(l1,l2))