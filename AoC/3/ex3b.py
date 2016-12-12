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

line=fin.readline()

iteration=0
triangleOk=0
triangleNok=0
triMatrix=[[],[],[]]
while len(line)>0:
    triArr=line.split()
    if len(triArr) == 3:
        iteration+=1
        triArr=map(lambda x:int(x),triArr)
        print "%s" % triArr
        for i in xrange(3):
            triMatrix[i].append(triArr[i])
        if  iteration%3==0:
            print "%s" % triMatrix
            for i in xrange(3):
                triMatrix[i].sort()
                if triMatrix[i][0]+triMatrix[i][1] > triMatrix[i][2]:
                    triangleOk+=1
                else:
                    triangleNok+=1
            triMatrix=[[],[],[]]
    #if iteration==30:
        #sys.exit(0)
    line=fin.readline()

print "iter: %d, ok: %d, nok: %d" % (iteration,triangleOk,triangleNok)
