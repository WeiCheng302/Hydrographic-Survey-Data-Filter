import numpy as np
polation=open("interpolation2.txt",'r')

out=open("delete3",'w')
n=0
for i in polation:
    polation4 = i.split(',')
    temp1=polation4
    n+=1
    print n
    check2=0

    while float(temp1[2]) < -1 and float(temp1[2]) > -50:
            check2=1
            break

    if check2 == 1:
        string="%f,%f,%f\n"%(float(temp1[0]),float(temp1[1]),float(temp1[2]))
        out.write(string)

out.close()