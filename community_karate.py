import networkx as nx 
import matplotlib.pyplot as plt
g=nx.karate_club_graph()

import matplotlib as mpl
mpl.use('tkagg')

labels=nx.get_node_attributes(g,'club')


from networkx.algorithms import community

com=community.girvan_newman(g)
list=tuple(sorted(c) for c in next(com))
print(list[0])
print(list[1])

pos=nx.spring_layout(g)


nx.draw_networkx_nodes(g, pos, nodelist=list[0], node_shape='^',node_color='b', alpha=0.5)
nx.draw_networkx_nodes(g, pos, nodelist=list[1], node_color='g', alpha=0.5)
nx.draw_networkx_labels(g, pos, labels=labels)
nx.draw_networkx_edges(g, pos, alpha=0.4, edge_color='C')
plt.show()
#plt.savefig("karate_com.eps")

