#class that implements an edge between two nodes
class Edge:
    import random

    label = 0 #distance between the two nodes
    firstNode = "" #the first node of the edge
    secondNode = ""#the second node of the edge
    status = ""#status of the edge (blocked/notblocked)
    blockageProbability = 0 #probability of the edge being blocked (0 - not blocked| 1 - blocked)

    def __init__(self,firstNode,secondNode,label):
        self.firstNode = firstNode
        self.secondNode = secondNode
        self.label = label
    
    def getFirstNode(self):
        return self.firstNode
    
    def getSecondNode(self):
        return self.secondNode
    
    def getLabel(self):
        return self.label
    
    def getBlockageProbability(self):
        return self.blockageProbability

    def setBlockageProbability(self,newProbabilityValue):
        self.blockageProbability = newProbabilityValue


#class that implements the graph representing the dataset
class Graph:

    numNodes = 0 #number of nodes in the graph
    numEdges = 0 #number of edges in the graph 
    edges = [] #list that contains the edges of the graph
    blockedEdges = [] #list that contains the blocked edges of the graph


    def __init__(self,numNodes):
        self.numNodes = numNodes

    def addEdge(self,node1,node2,label):
        self.numEdges += 1
        edge = Edge(node1,node2,label)
        self.edges.append(edge)
    
    def edgeExists(self,node1,node2):
        for element in self.edges:
            if (element.getFirstNode() == node2 and element.getSecondNode() == node1) or (element.getFirstNode() == node1 and element.getSecondNode() == node2):
                return element

    def removeEdge(self,edge):
        self.edges.remove(edge)

    def outAdjacentNodes(self,node):
        outNodes = []
        for edge in self.edges:
            if edge.getFirstNode() == node:
                outNodes.append(edge.getSecondNode())
        return outNodes
    
    def outAdjacentEdges(self,node):
        outEdges = []
        for edge in self.edges:
            if edge.getFirstNode() == node or edge.getSecondNode() == node:
                outEdges.append(edge)
        return outEdges
           


#class that implements the Dijkstra Algorith in a graph-based dataset
class UCTOAlgorithm:
    
    import heapq
    import random
    import math

    nodes = ["Oradea","Zerind","Sibiu","Arad","Timisoara","Lugoj","Mehadia","Dobreta","Craiova","Pitesti","Rimnicu","Bucharest","Fagaras","Giurgiu","Urziceni","Hirsova","Vaslui","Eforie","Iasi","Neamt","R.Vilcea"]
    selected = {} #dictionary with City:Boolean values representig the selected nodes
    numberOfCities = len(nodes) #number of cities of the dataset
    length = {}  #dictionary with the length of the shortest path between 2 cities 
    path = {} #dictionary with the shortest path between 2 cities
    dataset = [] #dataset with the cities
    connected = [] #cities already visited
    heapq.heapify(connected) #transform list into priority queue
    beliefSequence = [] #list that contains the final belief Sequence
    averageEstimatedCost = 0 #average estimated cost of N rollouts
    successfullRolloutsCost = [] #list with the cost of each successful rollout
    realityDataset = [] #real dataset the Canada driver is facing
    realityThreshold = round(random.uniform(0.7,1),1) #real treshold
    realityShortestPath = [] #final shortest path

    def __init__(self,numberOfRollouts,origin,destination): 
        self.averageEstimatedCost = self.math.floor(self.computeAlgorithm(numberOfRollouts,origin,destination))        
        self.realityDataset = Graph(self.numberOfCities)
        self.realityDataset.addEdge("Arad","Sibiu",140)
        self.realityDataset.addEdge("Arad","Timisoara",118)
        self.realityDataset.addEdge("Arad","Zerind",75)
        self.realityDataset.addEdge("Bucharest","Fagaras",211)
        self.realityDataset.addEdge("Bucharest","Giurgiu",90)
        self.realityDataset.addEdge("Bucharest","Pitesti",101)
        self.realityDataset.addEdge("Bucharest","Urziceni",85)
        self.realityDataset.addEdge("Craiova","Dobreta",120)
        self.realityDataset.addEdge("Craiova","Pitesti",138)
        self.realityDataset.addEdge("Craiova","R.Vilcea",146)
        self.realityDataset.addEdge("Dobreta","Mehadia",75)
        self.realityDataset.addEdge("Eforie","Hirsova",86)
        self.realityDataset.addEdge("Fagaras","Sibiu",99)
        self.realityDataset.addEdge("Hirsova","Urziceni",98)
        self.realityDataset.addEdge("Iasi","Neamt",87)
        self.realityDataset.addEdge("Iasi","Vaslui",92)
        self.realityDataset.addEdge("Lugoj","Mehadia",70)
        self.realityDataset.addEdge("Lugoj","Timisoara",111)
        self.realityDataset.addEdge("Oradea","Sibiu",151)
        self.realityDataset.addEdge("Oradea","Zerind",71)
        self.realityDataset.addEdge("Pitesti","R.Vilcea",97)		
        self.realityDataset.addEdge("R.Vilcea","Sibiu",80)
        self.realityDataset.addEdge("Urziceni","Vaslui",142)
        for edge in self.realityDataset.edges:
                edge.setBlockageProbability(round(self.random.uniform(0,1), 1))
                if edge.getBlockageProbability() >= self.realityThreshold:
                    self.realityDataset.removeEdge(edge)
        self.connected.clear()
        self.length.clear()
        self.path.clear()
        self.selected.clear()
        current = origin
        newEdges = []
        self.realityShortestPath.append(current)
        for node in self.beliefSequence:
            for outEdge in self.dataset.outAdjacentEdges(node):
                other = ""
                if node == outEdge.getFirstNode():
                    other = outEdge.getSecondNode()
                else:
                    other = outEdge.getFirstNode()
                if other in self.beliefSequence:
                    newEdges.append(self.realityDataset.edgeExists(node,other))
        self.realityDataset.edges.clear()
        self.realityDataset.edges = newEdges
        finalValue = self.computeDjikstra(self.realityDataset,origin,destination)
        if finalValue == 2e32:
            print("Unable to find a shortest path")
            self.realityShortestPath = []
        else:
            self.realityShortestPath = self.getPath(self.path,origin,destination)


#Method that computes the UCTO algorithm
    def computeAlgorithm(self,numberOfRollouts,origin,destination):
        self.beliefSequence.append(origin)
        counter = 0
        current = self.beliefSequence[counter]
        for rollout in range(numberOfRollouts):
            if current == destination:
                break
            self.dataset = Graph(self.numberOfCities)
            self.dataset.addEdge("Arad","Sibiu",140)
            self.dataset.addEdge("Arad","Timisoara",118)
            self.dataset.addEdge("Arad","Zerind",75)
            self.dataset.addEdge("Bucharest","Fagaras",211)
            self.dataset.addEdge("Bucharest","Giurgiu",90)
            self.dataset.addEdge("Bucharest","Pitesti",101)
            self.dataset.addEdge("Bucharest","Urziceni",85)
            self.dataset.addEdge("Craiova","Dobreta",120)
            self.dataset.addEdge("Craiova","Pitesti",138)
            self.dataset.addEdge("Craiova","R.Vilcea",146)
            self.dataset.addEdge("Dobreta","Mehadia",75)
            self.dataset.addEdge("Eforie","Hirsova",86)
            self.dataset.addEdge("Fagaras","Sibiu",99)
            self.dataset.addEdge("Hirsova","Urziceni",98)
            self.dataset.addEdge("Iasi","Neamt",87)
            self.dataset.addEdge("Iasi","Vaslui",92)
            self.dataset.addEdge("Lugoj","Mehadia",70)
            self.dataset.addEdge("Lugoj","Timisoara",111)
            self.dataset.addEdge("Oradea","Sibiu",151)
            self.dataset.addEdge("Oradea","Zerind",71)
            self.dataset.addEdge("Pitesti","R.Vilcea",97)		
            self.dataset.addEdge("R.Vilcea","Sibiu",80)
            self.dataset.addEdge("Urziceni","Vaslui",142)
            threshold = round(self.random.uniform(0.7,1),1) #threshold
            for edge in self.dataset.edges:
                edge.setBlockageProbability(round(self.random.uniform(0,1), 1))
                if edge.getBlockageProbability() >= threshold:
                    self.dataset.removeEdge(edge)  
            weather = self.computeDjikstra(self.dataset,current,destination)
            if weather == 2e32:
                self.dataset.edges.clear()
                continue
            else:
                for outAdjacentEdge in self.dataset.outAdjacentEdges(current):
                    differentNode = ""
                    if current == outAdjacentEdge.getSecondNode():
                        differentNode = outAdjacentEdge.getFirstNode()
                    else:
                        differentNode = outAdjacentEdge.getSecondNode()
                    if differentNode in self.beliefSequence:
                        continue
                    else:
                        if differentNode != self.computeLowestCost(current):
                            continue
                        else:
                            self.beliefSequence.append(differentNode) 
                            self.successfullRolloutsCost.append(weather)    
                            counter += 1
                            current = self.beliefSequence[counter]                            
            self.dataset.edges.clear()
            self.connected.clear()
            self.length.clear()
            self.path.clear()
            self.selected.clear()
        averageCost = self.averageCost(len(self.successfullRolloutsCost),self.successfullRolloutsCost)
        return averageCost

#Method that returns the estimated average cost of N successfull rollouts
    def averageCost(self,numberOfSuccessfullRollouts,rollouts):
        totalSum = 0
        for rolloutCost in rollouts:
            totalSum += rolloutCost
        return totalSum / numberOfSuccessfullRollouts

#Method that allows to return the lowest cost node of a set of successors of a node
    def computeLowestCost(self,node):
        distances = []
        finalValue = 0
        for outAdjacentEdge in self.dataset.outAdjacentEdges(node):
            distances.append(outAdjacentEdge.getLabel())
        minimumDistance = min(distances)
        for outAdjacentEdge in self.dataset.outAdjacentEdges(node):
            if minimumDistance == outAdjacentEdge.getLabel():
                if outAdjacentEdge.getFirstNode() == node:
                    finalValue = outAdjacentEdge.getSecondNode()
                else:
                    finalValue = outAdjacentEdge.getFirstNode()
                break
        return finalValue

#Method that allows to explore a node (used for Djikstra Algorithm)
    def exploreNode(self,dataset,node):
        for edge in dataset.outAdjacentEdges(node):
            if node == edge.getSecondNode():
                secondNode = edge.getFirstNode()
            else:
                secondNode = edge.getSecondNode()
            if self.selected[secondNode] == False:
                newLength = self.length[node] + edge.getLabel()
                if newLength < self.length[secondNode] :
                    nodeIsInQueue = self.length[secondNode] < 2e32 
                    self.length[secondNode] = newLength
                    self.path[secondNode] = node
                    if nodeIsInQueue == True:
                        self.connected.remove(self.connected[0])
                        self.heapq.heapify(self.connected)
                        self.heapq.heappush(self.connected,(newLength,secondNode))
                    else:
                        self.heapq.heappush(self.connected,(newLength,secondNode))

#Method that computes the Djikstra Algorithm
#Returns the length of the shortest path between 2 points
    def computeDjikstra(self,dataset,origin,destination):
       for node in self.nodes:
            self.selected[node] = False
            self.length[node] = 2e32
       self.length[origin] = 0
       self.path[origin] = origin
       self.heapq.heappush(self.connected,(0,origin))
       minimumNode = self.heapq.heappop(self.connected)
       cityChosen = minimumNode[1]
       self.selected[cityChosen] = True
       self.exploreNode(dataset,cityChosen)
       while len(self.connected) > 0:
            minimumNode = self.heapq.heappop(self.connected)
            cityChosen = minimumNode[1]
            self.selected[cityChosen] = True
            self.exploreNode(dataset,cityChosen)
       
       return self.length[destination]

#Method that returns the shortest path 
    def getPath(self,via,origin,destination):
        finalPath = []
        node = destination
        while node != origin:
            finalPath.append(node)
            node = via[node]
        finalPath.append(node)
        return finalPath

#main class of the program
class Main:
    ucto = UCTOAlgorithm(10000,"Arad","Bucharest")
    print("The Estimated Average Cost is: " + str(ucto.averageEstimatedCost))
    print("The Belief State has the states: " + str(ucto.beliefSequence))
    print("The Shortest Path is: " + str(ucto.realityShortestPath))
