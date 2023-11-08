#from numpy.random import *
import random
import sys, os, os.path
from networkx import *

# read network
g=read_edgelist(sys.argv[1])

# model parameters
beta=0.1 # infection rate
r=1 #recovery rate



# random seed node selection
num_seed=10


inf={} #dictionary for infected node
for i in random.sample(list(g.nodes()),num_seed):
    inf[i]=1    

 



max_count = 10000
num_r=0
print(0,len(g.nodes()),len(inf),0,len(inf))
for time in range(1,max_count):
    inflist=list(inf.keys())
    random.shuffle(inflist)
    for v in inflist:
        for nbr in g[v]:
            if nbr not in inf:
                if (random.random()<beta):
                    inf[nbr]=1
        if(random.random()<r):
            del inf[v]
            g.remove_node(v)
            num_r+=1
    num_inf=num_r+len(inf)
    # time, num of S nodes, num of I nodes, num of R nodes, num of I+R nodes
    print(time,len(g.nodes()),len(inf),num_r,num_inf)
    if len(inf)==0:
        break




            
