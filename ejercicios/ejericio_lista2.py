from re import L


l=[[4,12,5,66], [14,6,25], [3,4,5,67,89,23,1], [78,56]]

print(l)

for k in range(len(l)):
    for x in range(len(l[k])):
        if l[k][x]>10:
            l[k][x]=0
            
print(l)