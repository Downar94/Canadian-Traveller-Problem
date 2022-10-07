import random
from graphics import *



class Graph:
    nodenames = [] #nodes names (position in table = node number)
    edges = [] #edges in form [number_node1, number_node_2, distance]

    def __init__(self,nodenames):
        self.nodenames = nodenames

    def __getitem__(self,index):
        return self.edges[index]

    def __setitem__(self,index,index2,value):
        self.edges[index][index2] = value

    def __len__(self):
        return len(self.edges)

    def getNodenames(self):
        return self.nodenames

    def addEdge(self,node1name,node2name,distance,blockingProbability):
        self.edges.append([self.nodenames.index(node1name),self.nodenames.index(node2name),distance,blockingProbability])

    def removeEdge(self,node1name,node2name,distance,blockingProbability):
        self.edges.remove([self.nodenames.index(node1name),self.nodenames.index(node2name),distance,blockingProbability])

    def getNeighbours(self, node):
        neighbours = []
        for [n1,n2,d,b] in self.edges:
            if n1 == node: neighbours.append(n2)
            if n2 == node: neighbours.append(n1)
        return neighbours

    def getDist(self,node1,node2):
        for [n1,n2,d,b] in self.edges:
            if n1 == node1 and n2 == node2: return d
            if n2 == node1 and n1 == node2: return d

    

    def computeShortestPath(self,originName):
        q = list(range(len(self.nodenames))) #[0,1,2,3…,len(nodes)]

        #for each vertex v in Graph:
        #dist[v] ← INFINITY
        #prev[v] ← UNDEFINED
        #add v to Q
        dist = [9999999999] * len(self.nodenames)
        prev = [None] * len(self.nodenames)

        #dist[source] ← 0
        dist[self.nodenames.index(originName)] = 0

        #while Q is not empty:
        while len(q) > 0:
        #u ← vertex in Q with min dist[u]
            mindist = 99999999
            for qel in q:
                if dist[qel]  < mindist:
                    mindist = dist[qel]
                    u = qel


        #remove u from Q
            q.remove(u)

        #for each neighbor v of u:
            for v in self.getNeighbours(u):
        #alt ← dist[u] + length(u, v)
                alt = dist[u] + self.getDist(u,v)
        #if alt < dist[v]:
                if alt < dist[v]:
                #dist[v] ← alt
                #prev[v] ← u
                    dist[v] = alt
                    prev[v] = u

        return dist, prev

#main class of the program
def calculate():
    g = Graph(["Oradea","Zerind","Sibiu","Arad","Timisoara","Lugoj","Mehadia","Dobreta","Craiova","Pitesti","Bucharest","Fagaras","Giurgiu","Urziceni","Hirsova","Vaslui","Eforie","Iasi","Neamt","R.Vilcea"])
    g.addEdge("Arad","Sibiu",140,0)
    g.addEdge("Arad","Timisoara",118,0)
    g.addEdge("Arad","Zerind",75,0)
    g.addEdge("Bucharest","Fagaras",211,0)
    g.addEdge("Bucharest","Giurgiu",90,0)
    g.addEdge("Bucharest","Pitesti",101,0)
    g.addEdge("Bucharest","Urziceni",85,0)
    g.addEdge("Craiova","Dobreta",120,0)
    g.addEdge("Craiova","Pitesti",138,0)
    g.addEdge("Craiova","R.Vilcea",146,0)
    g.addEdge("Dobreta","Mehadia",75,0)
    g.addEdge("Eforie","Hirsova",86,0)
    g.addEdge("Fagaras","Sibiu",99,1)
    g.addEdge("Hirsova","Urziceni",98,0)
    g.addEdge("Iasi","Neamt",87,0)
    g.addEdge("Iasi","Vaslui",92,0)
    g.addEdge("Lugoj","Mehadia",70,0)
    g.addEdge("Lugoj","Timisoara",111,0)
    g.addEdge("Oradea","Sibiu",151,0)
    g.addEdge("Oradea","Zerind",71,0)
    g.addEdge("Pitesti","R.Vilcea",97,0)		
    g.addEdge("R.Vilcea","Sibiu",80,0)
    g.addEdge("Urziceni","Vaslui",142,0)

    rnumber = [random.randint(0, len(g)-1) for x in range(random.randint(1,5))]

    resultBlockedArray = []

    for block in rnumber:
        g[block][2] = 9999 
        resultBlockedArray.append([g[block][0],g[block][1]])   
    
    

    names = g.getNodenames()

    #starting place
    origin = "Oradea"
    originpos = names.index(origin)
    dist, prev = g.computeShortestPath(origin)

    #destination
    destination = "Eforie"
    destinationpos = names.index(destination)
    nodepos = destinationpos
    arr = []
    resultArr = []
    
    

    while nodepos != originpos:
        p = prev[nodepos]
        arr.append([names[nodepos],names[p],int(g.getDist(nodepos, p))])
        resultArr.append([nodepos,p])
        nodepos = p
        
    
    
    for x in range(0, len(arr)):
        if arr[x][2] == 9999: 
            print("There is no traversable road")
            return False, resultBlockedArray

    for x in range(0, len(arr)):
        print("EDGE: " + arr[x][0] + " — " + arr[x][1] + " with length " + str(arr[x][2]))
   
        
    
    return resultArr, resultBlockedArray

    
    


