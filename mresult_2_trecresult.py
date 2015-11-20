num_name = {}
with open ('names') as f:
    for l in f:
        l = l.split(',')
        l[1] = l[1].split('/')[-1]
        l[1] = l[1].split('.')[0]
        num_name[int(l[0])] = l[1][:-1]
with open('matlab_output.csv') as f:
    trec_results = []
    for line in f:
        print line
        line = line.split(',')
        q = line[0]
        k = 40.
        for i,r in enumerate(line[1:]):
            trec_results.append(' '.join([q,num_name[int(r)],'1',str(k-i),'bp']))
q = open('m_results.eval','w')
q.write('\n'.join(trec_results))
