import numpy as np
from scipy.special import psi
from scipy import sparse
from sys import getsizeof
import cPickle as pickle
import csv
import os

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

    if 'index.p' not in os.listdir('./'):
        size = file_len('postings_m')
        index = np.zeros([size,3])
        with open('postings_m') as f:
            for i,l in enumerate(f):
                index[i,:] = map(int,l.split('\t'))
        print ('finished reading in postings')
        # index = np.loadtxt('postings_m',dtype=np.uint32)
        index = sparse.csc_matrix((index[:,2], (index[:,0]-1,index[:,1]-1)) ,dtype=np.uint32)
        f = open('index.p','wb')
        pickle.dump(index,f)
    else:
        f = open('index.p','r')
        index = pickle.load(f)
    f.close()
    print ('finished loading sparse')
    if 'lengths.p' not in os.listdir('./'):
        data = np.loadtxt('lengths',delimiter = ',',usecols=(1,))
        # doclengths = np.reshape(data,[len(data),1])
        f = open('lengths.p','wb')
        pickle.dump(data,f)
    else:
        f = open('lengths.p','r')
        data = pickle.load(f)
    f.close()

    print("finished reading lengths")
    #build map with key -> begin,end



    return index,data

def mapping():
    if 'map.p' in os.listdir('./'):
        f = open('map.p','r')
        m = pickle.load(f)
        f.close()
        print('loaded mapping')
        return m
    fin_id = -1
    idd=0
    m = {}
    run = 0
    with open('postings') as f:
        line1 = f.readline()
        line2 = f.readline()
        while(line1):
	    run += 1
            if run % 100000 == 0:
		print run,
            word1 = line1.split(',')[0]
            word2 = line2.split(',')[0]
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
    print "done"
    f = open('map.p','wb')
    pickle.dump(m,f)
    f.close()
    return m

def bcb(qtok,index,doclengths,m):
    """takes in q,index,doclength,m and outputs top scoring documents"""
    x = np.shape(doclengths)[0]
    score = np.zeros((x))
    for q in qtok:
        print q,
        if q not in m:
            continue
        ind = m[q]
        #map whatever matrix to sparse namespace
        #use columns, now sure yet
        tf_q = np.reshape(index[ind[0]:ind[1]+1,:].getnnz(1)-1,[ind[1]-ind[0]+1,1])
        tf_q[tf_q<=0] = 1
        B = np.ones((ind[1]-ind[0]+1,2))*.5
        used_docs = index[ind[0]:ind[1]+1,0].todense()
        tf = np.append(tf_q,doclengths[used_docs]-tf_q,axis=1)
        error = np.array([[10,10]])
        a = 0.003
        tol = 0.001
        while np.any(error > tol):
            gl = psi(np.sum(B,1))-psi(np.sum(tf,1)+np.sum(B,1))
            B_old = B
            B = B + a *(np.array([gl,gl]).T + psi(tf+B) - psi(B))
            error = np.max(B-B_old)
        score[used_docs.T] = score[used_docs.T] + np.sum((tf-1 * B + (tf-1)*(tf)/2.),axis=1)
    n = 40
    print ''
    final = score.argsort()[::-1][:n]
    for i,idx in enumerate(final):
        if score[idx] == 0:
            return final[:i]


def evaluate(fil_name):
    index,doclengths = index_in()
    m = mapping()
    f = open(fil_name,'r')
    queries = f.readlines()
    results = np.zeros([len(queries),41])
    run = 0
    for q in queries:
        q = q.split()
        print run,
        results[run,0] = q[0]
        results[run,1:]=bcb(q[1:],index,doclengths,m)
        run +=1
    np.savetxt('python_results',results) 


if __name__ == '__main__':
    m = mapping()
    index,doclengths = index_in()
    evaluate('rob04.titles.tsv')
