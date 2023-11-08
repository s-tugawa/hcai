import sys
import networkx as nx

def each_line(filename):
    with open(filename, encoding='utf-8') as f:
        for line in f:
            yield line.rstrip('\r\n')

gfile=sys.argv[1]
cfile=sys.argv[2]

g=nx.read_edgelist(gfile)

deg=nx.degree_centrality(g)


pr = nx.pagerank(g)

kcore=nx.core_number(g)
print("node_id citation degree PageRank k-core")
for line in each_line(cfile):
    [u,c]=line.split(" ")
    print(u,c,deg[u],pr[u],kcore[u])
