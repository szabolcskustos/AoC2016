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
passcode=[]
while len(passcode)<8:
    m=md5.new()
    m.update(doorId+str(idx))

    md5str=m.hexdigest()

    #print "hash: %s" % m.hexdigest()

    if md5str[0:5] == "00000":
        print "ok hash:%s part %s" % (md5str, md5str[5:6])
        passcode.append(md5str[5:6])

    idx+=1

print "passcode: %s" % passcode
#line=fin.readline()



