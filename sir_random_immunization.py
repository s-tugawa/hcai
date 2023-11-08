#from numpy.random import *
import random
import sys, os, os.path
from networkx import *

# read network
g=read_edgelist(sys.argv[1])

# model parameters
beta=0.04 # infection rate
r=0.2 #recovery rate



#frac_vaccine=0.1
frac_vaccine=0
num_vaccinated=len(g.nodes)*frac_vaccine

vaccinated_nodes=random.sample(list(g.nodes()),int(num_vaccinated))
for i in vaccinated_nodes:
    g.remove_node(i)
                       



inf={} #dictionary for infected node
# A randomly selected node becomes infected
i = random.choice(list(g.nodes()))
inf[i]=1




max_count = 10000
num_r=0
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




            
