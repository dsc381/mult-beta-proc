import os,sys
f = open(sys.argv[1],'r')
converted = []
row = 0
for line in f:
    row += 1
    line = line[:-1].split(',')
    col = 0
    for entry in line[1:]:
        col+=1
        converted.append(str(row)+'\t'+str(col)+'\t'+entry+'\n')
f.close()
f = open('postings_m','w')
f.write(''.join(converted))


