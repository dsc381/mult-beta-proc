import os,sys
import os

import os
import psutil

process = psutil.Process(os.getpid())
mem = psutil.virtual_memory()
ram = mem.total  # total physical memory available
GB = 2**30
cutoff = (ram*.001)/GB
print cutoff
f = open(sys.argv[1],'r')
q = open('postings_m','w')
converted = []
row = 0
for line in f:
    row += 1
    if (row%1000 == 0 and process.memory_info().rss/(2**20) > cutoff):
        print "clearing ram"
        q.write(''.join(converted))
        converted = []
    line = line[:-1].split(',')
    col = 0
    for entry in line[1:]:
        col+=1
        converted.append(str(row)+'\t'+str(col)+'\t'+entry+'\n')
f.close()
q.write(''.join(converted))


