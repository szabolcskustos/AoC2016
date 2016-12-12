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


steps={
    "R":[1,0],
    "L":[-1,0], 
    "U":[0,1],
    "D":[0,-1]
}


position=[0,0]


def stepWithLimit(direction):
    for i in xrange(2):
        if position[i]+steps[direction][i] <= 1 and \
            position[i]+steps[direction][i] >=-1:
            position[i]+=steps[direction][i]
            

while len(line)>0:
    #print "step: %s" % step
    line=line.strip()
    if len(line)>0:
        for i in xrange(len(line)):
            stepWithLimit(line[i])
    print "position: %s" % position
    line=fin.readline()
#print "positionArr: %s" % positionArr
#print "pos: %s" % position

