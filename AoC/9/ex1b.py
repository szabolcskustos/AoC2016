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




line=fin.readline().strip()

decompressedSize=0

decompressMode=0
markerMode=False

marker=[]
factorArr=[1]
lenArr=[]
for i in xrange(len(line)):
    c=line[i]
    print "%s " %c ,
    if "(" == c:
        markerMode=True
        marker=[]
    elif ")" == c and markerMode:
        markerArr= ("".join(marker)).split("x")
        lenArr.append(int(markerArr[0])+i)
        factorArr.append(int(markerArr[1])*factorArr[-1])
        markerMode=False
    elif markerMode:
        marker.append(c)
    else:
        print "factor: %d" % factorArr[-1]
        decompressedSize+=factorArr[-1]
    while 0 < len(lenArr) and lenArr[-1]<=i:
        del lenArr[-1]
        del factorArr[-1]
               
print "decompressed size: %d" % decompressedSize
#while len(line) :
#print "ones: %d" % ones
#line=fin.readline()



