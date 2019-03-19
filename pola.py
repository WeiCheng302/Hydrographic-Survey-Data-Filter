import numpy as np
polation=open("delete3.txt",'r')
polation2=open("delete4.txt",'r')

out=open("polationout20007",'w')
n=0
for i in polation:
    polation4 = i.split(',')
    temp1=polation4
    k = polation2.readline()
    n+=1
    print n
    polation6 = k.split(',')
    temp2=polation6
    check1=0
    check2=0
    while temp1[0] == temp2[0] and temp1[0] == temp2[0] :
            check1=1
            break
    while temp1[0] != temp2[0] or temp1[1] != temp2[1] :
            check2=1
            break
    if check2 == 1:
        string="%f,%f,%f\n"%(float(temp1[0]),float(temp1[1]),float(temp1[2]))
        out.write(string)

out.close()