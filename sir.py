from numpy.random import *
import sys, os, os.path
from networkx import *

# read network
g=read_edgelist(sys.argv[1])

# model parameters
beta=0.04 # infection rate
r=0.2 #recovery rate

inf={} #dictionary for infected node
# A randomly selected node becomes infected
i = choice(list(g.nodes()))
inf[i]=1

max_count = 10000
num_r=0
for time in range(1,max_count):
    inflist=list(inf.keys())
    shuffle(inflist)
    for v in inflist:
        for nbr in g[v]:
            if nbr not in inf:
                if (random()<beta):
                    inf[nbr]=1
        if(random()<r):
            del inf[v]
            g.remove_node(v)
            num_r+=1
    num_inf=num_r+len(inf)
    # time, num of S nodes, num of I nodes, num of R nodes, num of I+R nodes
    print(time,len(g.nodes()),len(inf),num_r,num_inf)
    if len(inf)==0:
        break




            
