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

codes=[ ['X','X','1','X','X'],
        ['X','2','3','4','X'],
        ['5','6','7','8','9'],
        ['X','A','B','C','X'],
        ['X','X','D','X','X']  ]


steps={
    "R":[1,0],
    "L":[-1,0], 
    "U":[0,1],
    "D":[0,-1]
}


position=[0,0]


def stepWithLimit(direction):
    dist=[0,0]
    for i in xrange(2):
        dist[i]=position[i]+steps[direction][i]
        if dist[i]<0:
            dist[i]*=-1
    #print "dist: %s dir:%c" % (dist,direction)
    r=reduce(lambda x,y: x+y,dist)
    if r<=2:
        for i in xrange(2):
            position[i]+=steps[direction][i]
        #print "posmiddle: %s" % position

def pos2Code(pos):
    return codes[pos[1]*-1+2][pos[0]+2]

stepArr=[]
while len(line)>0:
    #print "step: %s" % step
    line=line.strip()
    if len(line)>0:
        j=0
        for i in xrange(len(line)):
            j+=1
            stepWithLimit(line[i])
            stepArr.append(line[i])
            if j%5==0:
                #print "%s, %s" % (stepArr, position)
                stepArr=[]

    #print "%s, %s" % (stepArr, position)
    print "position: %s,  %s" % (position, pos2Code(position))
    #sys.exit(1)
    line=fin.readline()
#print "positionArr: %s" % positionArr
#print "pos: %s" % position

