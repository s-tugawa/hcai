import sys
import networkx as nx 

def each_line(filename):
    with open(filename, encoding='utf-8') as f:
        for line in f:
            yield line.rstrip('\r\n')



file=sys.argv[1]
g=nx.read_edgelist(file)
label_f=sys.argv[2]
label_id={}
for l in each_line(label_f):
    [v,label]=l.split(" ")
    label_id[v]=int(label)

from networkx.algorithms.community import greedy_modularity_communities
c=list(greedy_modularity_communities(g))

id=0
com_id={}
for com in c:
    id+=1
    for v in sorted(com):
#        print(v,id)
        com_id[v]=id
com_list=[]
label_list=[]
for v in g.nodes():
    com_list.append(com_id[v])
    label_list.append(label_id[v])
    print(v,com_id[v],label_id[v])


from sklearn.metrics.cluster import rand_score
print(rand_score(com_list,label_list))
