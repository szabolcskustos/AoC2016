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

summ=0
iteration=0
while len(line) > 0:
    iteration+=1
    if len(line.strip()):
        codeDict=dict()
        lineArr=line.strip().split("-")
        codes=lineArr[0:-1]
        cksumArr=lineArr[-1:]
        cksumArr=cksumArr[0].split("[")
        cksumArr[1]=cksumArr[1][0:-1]
        codesOrig=list("-".join(codes))
        codes="".join(codes)

        for c in codes:
            codeDict[c]=codeDict.get(c,0)+1

        codeList=[(v,k) for k,v in codeDict.iteritems()]
        codeList.sort(key=lambda x:(x[0],-ord(x[1])), reverse=True)
        valid=True
        for c in cksumArr[1]:
            if codeList:
                item=codeList.pop(0)
                #print "%s, %s" % (c, item)
                if c!=item[1]:
                    valid=False
            else:
                valid=False 
        if valid:
            summ+=int(cksumArr[0])
            for i in xrange(len(codesOrig)):
                if codesOrig[i]=='-':
                    if int(cksumArr[0])%2==1:
                        codesOrig[i]=' '
                else:
                    codesOrig[i]=chr( (ord(codesOrig[i])-ord('a')+int(cksumArr[0]))%26+ord('a') )
            print "%s, %d"% ("".join(codesOrig),int(cksumArr[0]))
        #print "%s, %s, %s, %s, %s" %(codes,cksumArr,codeList,codesOrig,valid)

    #if iteration > 10:
        #sys.exit(0)
    line=fin.readline()
print "sum: %d" %summ

