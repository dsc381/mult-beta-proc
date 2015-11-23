import numpy as np
from scipy.special import psi
from scipy import sparse
from sys import getsizeof
import csv

# def look_up_doc_tf(begin,end):
#     terms = []
#     lengths = []
#     doc = []
#     with open('postings') as f:
#         for i,l in enumerate(f):
#             #check to make sure its >= and not >
#             if i >= begin and i <= last:
#                 l = l.split(',')
#                 doc.append(int(l[1]))
#                 terms.append(l[2:])
#     with open('lengths') as f:
#         for i,d in enumerate(f):
#             if bisect.bisect(doc,i):
#                 lengths.append(int(d.split(',')[1]))


def index_in():
    def file_len(fname):
        with open(fname) as f:
            for i, l in enumerate(f):
                pass
        return i + 1

    size = file_len('postings_m')
    index = np.zeros([size,3])
    with open('postings_m') as f:
        for i,l in enumerate(f):
            index[i,:] = map(int,l.split('\t'))
    # index = np.loadtxt('postings_m',dtype=np.uint32)
    print ('finished reading in postings')
    index = sparse.csc_matrix((index[:,2], (index[:,0]-1,index[:,1]-1)) ,dtype=np.uint32)
    print ('finished sparse')
    data = np.loadtxt('lengths',delimiter = ',',usecols=(1,))
    doclengths = np.shape(np.reshape(data,[len(data),1]))
    print("finished reading lengths")
    #build map with key -> begin,end



    return index

def mapping():
    fin_id = -1
    idd=0
    m = {}
    with open('postings') as f:
        line1 = f.readline()
        line2 = f.readline()
        while(line1):
            word1 = line1.split(',')[0]
            word2 = line2.split(',')[1]
            fin_id = fin_id+1
            start = idd;
            if word1 == word2:
                line1 = line2
                line2 = f.readline()
                continue
            idd = fin_id +1;
            fin = fin_id
            m[word1]=[start,fin]
            line1 = line2
            line2 = f.readline()
        m[word1] = [start,fin_id+1]
    return m

def bcb(q):
    qtok = q.split()
    score = np.zeros(length(doclengths),1)
    for q in qtok:
        if q not in m:
            continue
        ind = m(q)
        #map whatever matrix to sparse namespace
        #use columns, now sure yet
        tf_q = sparse.nnz(index[ind(1):ind(2),:])-1
        tf_q[tf_q<=0] = 1
        B = ones(ind[2]-ind[1]+1,2)*.5
        tf = np.append(tf_q,doclengths[(index[ind(1):ind(2)]+1)],axis=1)
        error = np.array([[10,10]])
        a = 0.003
        while np.any(error > tol):
            gl = psi(np.sum(B,2))-psi(np.sum(tf,2)+np.sum(B,2))
            B_old = B
            B = B + a *(np.append(gl,gl,axis=1) + psi(tf+B) - psi(B))
            error = np.max(B-B_old,axis=0)
        score[doclengths[(index[ind(1):ind(2)]+1)]] = score[doclengths[(index[ind(1):ind(2)]+1)]] + np.sum((tf-1 * B + (tf-1)*(tf)))
    return np.argsort(score)[:40]

def evaluate(fil_name):
    f = open(fil_name,'r')
    queries = f.readlines()
    results = np.zeros([len(queries),40])
    run = 0
    for q in queries:
        print q
        results[run]=bcb(q.split()[1:])
        run +=1
    np.savetxt('python_results',results) 


if __name__ == '__main__':
    m = mapping()
