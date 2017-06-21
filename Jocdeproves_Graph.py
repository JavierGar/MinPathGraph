from Graph import *
g=Graph()
g.addNode('Barcelona')
g.addNode('Girona')
g.addNode('Tarragona')
g.addNode('Mollet')
g.addNode('Cerdanyola')
g.addNode('Terrassa')
g.addNode('Sabadell')
g.addNode('Manresa')
g.addNode('Cornella')
g.addEdge('Cornella','Sabadell',2)
g.addEdge('Barcelona','Cornella',22)
g.addEdge('Barcelona','Girona',99)
g.addEdge('Barcelona','Cerdanyola',21)
g.addEdge('Cerdanyola','Sabadell',10)
g.addEdge('Sabadell','Terrassa',12)
g.addEdge('Sabadell','Girona',33)
g.addEdge('Girona','Mollet',229)
g.addEdge('Barcelona','Mollet',163)
g.addEdge('Manresa','Mollet',115)
g.addEdge('Mollet','Tarragona',103)
g.addEdge('Tarragona','Manresa',103)
print g.getNodes()
print g.getEdges()
print g.getNeighbors('Barcelona')
print g.getNeighbors('Sabadell')
print g.getMinPath('Barcelona','Manresa')
print g.getMinPath('Barcelona','Tarragona')
print g.getMinPath('Cerdanyola','Terrassa')
print g.getMinPath('Sabadell','Mollet')