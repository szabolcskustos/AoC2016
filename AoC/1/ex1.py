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


R=[[0,1]  , [-1,0]]
L=[[0,-1] , [1,0 ]]

direction=[1,0]

position=[0,0]
positionArr=[[0,0]]

def changeDir(d):
    global R
    global L
    global direction
    if d =='L':
        act=L
    else:
        act=R

    ret=[0,0]
    for i in xrange(2):
        ret[i]=0
        for j in xrange(2):
            ret[i] += direction[j]*act[j][i]
    direction=ret
    return ret


print "R: %s %s %s %s" % (changeDir("R"),changeDir("R"),changeDir("R"),changeDir("R"))
print "L: %s %s %s %s" % (changeDir("L"),changeDir("L"),changeDir("L"),changeDir("L"))

stepArr=line.split(", ")

for step in stepArr:
    #print "step: %s" % step
    lr=step[0:1]
    dist=int(step[1:])
    changeDir(lr)
    for i in xrange(2):
       position[i]+=dist*direction[i]
    if position in positionArr:
        print "ok %s %s" % (position, positionArr)
    positionArr.append(list(position))
    #print "positionArr: %s" % positionArr
    print "lr: %c, step:%d" %(lr,dist)

print "positionArr: %s" % positionArr
print "pos: %s" % position

