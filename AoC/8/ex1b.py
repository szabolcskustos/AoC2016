#! /usr/bin/python

import sys
import math

if len(sys.argv) < 2:
	exit(1)

finname = sys.argv[1]
if ".in" in finname:
    foutname = finname.replace(".in",".out")
else:
    foutname = finname+".out"

print "{} {}".format(finname,foutname)

fin=open(finname,"r")
fout=open(foutname,"w")

screen=[[],[],[],[],[],[]]
for arr in screen:
    for i in xrange(50):
        arr.append(0)



line=fin.readline().strip()

while len(line) :
    lineArr=line.split(" ")
    if "rect"==lineArr[0]:
        dimArr=lineArr[1].split("x")
        for j in xrange(int(dimArr[1])):
            for k in xrange(int(dimArr[0])):
                screen[j][k]=1
    elif "column"==lineArr[1]:
        newCol=[0]*6
        actCol=int(lineArr[2][2:])
        shift=int(lineArr[4])
        for i in xrange(6):
            newCol[(i+shift)%6]=screen[i][actCol]
        for i in xrange(6):
            screen[i][actCol]=newCol[i]
    elif "row"==lineArr[1]:
        newRow=[0]*50
        actRow=int(lineArr[2][2:])
        shift=int(lineArr[4])
        for i in xrange(50):
            newRow[(i+shift)%50]=screen[actRow][i]
        for i in xrange(50):
            screen[actRow][i]=newRow[i]
    else:
        print "error"


    line=fin.readline().strip()

ones=0
for row in screen:
    part=reduce(lambda x,y: x+y, row)
    i=0
    for char in row:
        i+=1
        if 1==char:
            print "#",
        else:
            print ".",
        if i%5==0:
            print " ",
    print ""

    ones+=part
print "ones: %d" % ones 
#line=fin.readline()



