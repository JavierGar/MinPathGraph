import operator
class Graph (object):
    __slot__ = ['__nodes''__edges','__size']
    class Node(object):
        __slots__=['__data']
        def __init__(self, data): #datos del nodo
            self.__data = data
        def getData(self):
            return self.__data
        def __str__(self):
            return str(self.__data)
    class Edge (object):
        __slots__=['__start','__end','__data']
        def __init__(self, start, end, data): #edge necesita 3 variables, el valor de la aresta y los nodos que une
            self.__data = data
            self.__start = start
            self.__end = end
        def getData(self):
            return self.__data
        def getStart(self):
            return self.__start
        def getEnd(self):
            return self.__end
    def __init__(self):
        self.__nodes = []
        self.__edges = []
        self.__size = 0
    def addNode(self, data):
        self.__nodes.append(self.Node(data))  #añade el nodo a la lista y aumenta el tamaño
        self.__size += 1
    def addEdge(self, start, end, data):
        for i in self.__nodes:   #busca el nodo inicial
            if i.getData() == start :
                for j in self.__nodes: #busca el nodo final
                    if j.getData() == end :
                        self.__edges.append(self.Edge(i, j, data)) #añade a la lista de edges la nueva aresta, con
                        return                                         # los datos de la aresta y los nodos que une

    def getNodes(self):
        nodos = []
        for i in self.__nodes :
            nodos.append(i.getData())  #coge los datos de los nodos y los mete en una lista de python, para mostrarlos
        return nodos

    def getEdges(self):
        arestas = []
        for i in self.__edges : #recorremos cada sublista de la lista de listas
            parcial = []   #las arestas estan en una lista de listas, asi que hago una lista parcial para sacar
            x = i.getStart() #los datos y guardarlos por separado
            z = i.getEnd ()
            parcial.append(x.getData())  # añadimos los datos a la lista temporal
            parcial.append(z.getData())
            parcial.append(i.getData())
            arestas.append(parcial)   # guardamos los datos en una lista para mostrarlos
        return arestas

    def getNeighbors(self,nodedata):
        lista = Graph.getEdges(self) #guardamos todos los nodos
        neighbours = [] #guardaremos aqui los que nos interesen
        for sublist in lista: #recorremos cada sublista de la lista
            if sublist[0] == nodedata: #comprobamos si el primer dato, o nodo start es que el buscamos
                b = sublist[1]  # guardamos el nodo al que esta conectado
                c = sublist[2]  # y el valor de la arista
                for i in self.__nodes: #recorremos los nodos y sacamos los datos para compararlos con los valores
                    if i.getData() == b :  #que hemos obtenido antes, y guardamos el nodo, que es lo que necesitamos
                        tupla = (i, c) #los guardamos en una tupla y los metemos en una lista
                        neighbours.append(tupla)
        return neighbours  #para mosterarlos por pantalla

    def getMinPath(self, start, end):
        cont = 0
        distances = {} #distancias a cada no
        not_visited = {} #nodo esta visitado o no
        lista = Graph.getNodes(self) #nodos del grafo
        for i in lista :  #todas las distancias a valores altisimos menos el nodo actual
            distances[i] = 999999999  #son muy altos para las comparaciones de mas adelante
        distances[start] = 0
        for i in lista : #todos los nodos no visitados menos el nodo actual
            not_visited[i] = True
        not_visited[start] = False
        actual = start  #guardaremos el nodo actual , que de momento es el inicial
        camino = [actual] #metemos el nodo actual en una lista donde guardaremos el camino
        while not_visited[end] == True : #siempre que no hayamos llegado al final
            neighbors = Graph.getNeighbors(self,actual)
            vedist = {} #iniciamos un dict donde guardaremos distancias a vecinos
            if not neighbors: #si neighbors no contiene nada (callejon sin salida), haremos backtracking
                while cont != 0:  #como hacemos backtracking hay que borrar
                    del camino[-1] #los ultimos movimientos
                    cont -= 1
                backtrack = {}
                backtrack = [key for key, val in not_visited.items() if val==True] #guardamos los nodos no visitados
                for i in backtrack :
                    vedist [i] = distances [i] # y les añadimos las distancias
                del not_visited[actual]
                actual = min(vedist, key=vedist.get) #escogemos el mas cercano, lo añadimos al camino, se convierte
                not_visited[actual] = False  #en el actual y lo guardamos como visitado
                camino.append(actual)
                cont += 1
            else :  #si neighhbors no esta vacio
                if neighbors:
                    for sublist in neighbors:
                        node = sublist[0].getData()
                        if not_visited[node] == True :
                            d = distances[actual] + sublist [1]
                            if d < distances [node] : #guardamos las nuevas distancias
                                distances[node] = d
                vecinos = []
                vecinos = [key for key, val in not_visited.items() if val==True] #guardamos los vecinos no visitados
                for i in vecinos :
                    vedist [i] = distances [i] # y les añadimos las distancias
                del not_visited[actual]
                actual = min(vedist, key=vedist.get) #escogemos el mas cercano, lo añadimos al camino, se convierte
                not_visited[actual] = False #en el actual y lo guardamos como visitado
                camino.append(actual) #añadimos a la lista que guarda el camino
                cont += 1
        print camino #devolvemos el camino
        return distances[end] # y la distancia mas corta al nodo objetivo