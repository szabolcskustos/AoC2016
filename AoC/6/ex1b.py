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

passcode=[]
result=[]

print "passcode: %s" % passcode

line=fin.readline().strip()
for idx in xrange(len(line)):
    passcode.append(dict())
while len(line) :
    for idx in xrange(len(line)):
        print "idx: %d, line: %s" % (idx,line)
        orig=passcode[idx].get(line[idx],0)
        passcode[idx][line[idx]]=orig+1
    line=fin.readline().strip()

for dval in passcode:
    print "dval: %s" % (dval)
    minval=0
    minchar=""
    for k,v in dval.items():
        if   v<minval or minval==0:
            minchar=k
            minval=v
    result.append(minchar)



print "passcode: %s" % "".join(result)
#line=fin.readline()



