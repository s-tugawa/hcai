import sys
import networkx as nx

input=sys.argv[1]
g=nx.read_edgelist(input,create_using=nx.DiGraph)

#indegree
indeg=nx.in_degree_centrality(g)
#outdegree
outdeg=nx.out_degree_centrality(g)
#betweenness
bet=nx.betweenness_centrality(g)
#closeness
clo=nx.closeness_centrality(g)
#PageRank
pr = nx.pagerank(g)
#Coreness
kcore=nx.core_number(g)
for v in g.nodes():
    print(v,indeg[v],outdeg[v],bet[v],clo[v],pr[v],kcore[v])
