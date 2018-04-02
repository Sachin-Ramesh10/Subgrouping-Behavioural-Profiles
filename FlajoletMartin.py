import hashlib
files= ['quotes_2008-08.txt','quotes_2008-09.txt','quotes_2008-10.txt','quotes_2008-11.txt','quotes_2008-12.txt','quotes_2009-01.txt','quotes_2009-02.txt','quotes_2009-03.txt','quotes_2009-04.txt']
tails=0
for f in files:
    with open (f,'r',encoding='utf8') as in_file:
        for l in in_file:
            if(l[0]=='Q'):
                initialhash=hash(l)
                binaryhash=bin(initialhash)
                currenttail = (len(binaryhash) - len(binaryhash.rstrip('0')))
                if  currenttail > tails :
                    tails = currenttail
print("Largest number of tailing zeros is: {}.format(tails)")

distinct = 2**tails
print("The number of distinct elements: {}.format(distinct)")
print(distinct)