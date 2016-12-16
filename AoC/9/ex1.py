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
for c in line:
    if 0==decompressMode:
        if "(" == c:
            markerMode=True
            marker=[]
        elif ")" == c and markerMode:
            markerArr= ("".join(marker)).split("x")
            decompressMode=int(markerArr[0])
            decompressedSize+=decompressMode*int(markerArr[1])
            markerMode=False
        elif markerMode:
            marker.append(c)
        else:
            decompressedSize+=1
    else:
        decompressMode-=1
               
print "decompressed size: %d" % decompressedSize
#while len(line) :
#print "ones: %d" % ones
#line=fin.readline()



