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
while len(line)>0:
    iteration+=1
    triArr=line.split()
    triArr=map(lambda x:int(x),triArr)
    triArr.sort()
    print "triArr: %s " % (triArr)
    if len(triArr) ==3: 
        if triArr[0]+triArr[1] > triArr[2]:
            triangleOk+=1
        else:
            triangleNok+=1
    line=fin.readline()

print "iter: %d, ok: %d, nok: %d" % (iteration,triangleOk,triangleNok)
