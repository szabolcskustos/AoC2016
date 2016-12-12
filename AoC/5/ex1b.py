#! /usr/bin/python

import sys
import math
import md5

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

doorId=fin.readline().strip()
idx=0
remaining=8
passcode=dict()
while remaining>0:
    m=md5.new()
    m.update(doorId+str(idx))

    md5str=m.hexdigest()

    #print "hash: %s" % m.hexdigest()

    if md5str[0:5] == "00000":
        print "ok hash:%s part %s remaining: %d" % (md5str, md5str[5:7],remaining)
        position=ord(md5str[5:6])-ord('0')
        char=md5str[6:7]
        if position>=0 and position<8 and passcode.get(position)==None:
            passcode[position]=char
            remaining-=1

    idx+=1

print "passcode: %s" % "".join(passcode.values())
#line=fin.readline()



