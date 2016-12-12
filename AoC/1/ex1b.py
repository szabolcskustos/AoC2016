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

stepNr=0
for step in stepArr:
    #print "step: %s" % step
    stepNr+=1
    lr=step[0:1]
    dist=int(step[1:])
    changeDir(lr)
    for i in xrange(2):
       print "cond: %d" % (dist*direction[i])
       if dist*direction[i] != 0:
           factor=1
           if dist*direction[i] < 0:
               factor=-1 
           for j in xrange(dist*direction[i]*factor):
              newpos=list(position)
              newpos[i]=position[i]+(j+1)*factor
              if newpos in positionArr:
                  print "Ok: %s %s" % (newpos, positionArr ) 
              positionArr.append(newpos)
       position[i]+=dist*direction[i]
    print "lr: %c, step:%d position: %s" %(lr,dist, position)
    print "lr: %c, step:%d" %(lr,dist)
    #print "positionArr: %s" % positionArr

print "positionArr: %s" % positionArr
print "pos: %s" % position

