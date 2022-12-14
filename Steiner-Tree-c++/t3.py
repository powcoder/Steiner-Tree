https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
import networkx as nx
import csv
import matplotlib.pyplot as plt
Data = open('t3.csv', "r")
next(Data, None)  # skip the first line in the input file
Graphtype = nx.Graph()

G = nx.parse_edgelist(Data, delimiter=',', create_using=Graphtype,
                      nodetype=int, data=(('weight', float),))
pos = nx.spring_layout(G)
nx.draw(G,pos,edge_color='black',width=1,linewidths=1,\
node_size=500,node_color='pink',alpha=0.9,\
labels={node:node for node in G.nodes()})
#pos = nx.spring_layout(G)

#labelmap = dict(zip(G.nodes(), ["1", "2", "3", "4"]))
nx.draw_networkx_edge_labels(G,pos,edge_labels={(1,2):G[1][2]['weight'],(1,3):G[1][3]['weight'],(1,4):G[1][4]['weight'],(1,9):G[1][9]['weight'],(1,10):G[1][10]['weight'],(2,5):G[2][5]['weight'],(2,7):G[2][7]['weight'],(3,5):G[3][5]['weight'],(3,6):G[3][6]['weight'],(3,8):G[3][8]['weight'],(4,5):G[4][5]['weight'],(5,6):G[5][6]['weight'],(5,7):G[5][7]['weight'],(6,7):G[6][7]['weight'],(6,8):G[6][8]['weight'],(7,8):G[7][8]['weight'],(8,9):G[8][9]['weight'],(10,9):G[10][9]['weight'],(5,10):G[5][10]['weight'],(7,10):G[7][10]['weight']},font_color='red')
plt.show()

