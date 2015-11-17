import os,sys
PATH = sys.argv[1]
converted = []
f = open(PATH,'r')
for line in f:
    line = line.split('\t',1)
    converted.append(line[0]+', '+line[1])
f.close()
f = open(PATH+'_m','w')
f.write(''.join(converted))

    
