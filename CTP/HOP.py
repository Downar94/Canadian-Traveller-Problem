# I used A* shortest path algorithm,
# In function _hopHeuristic() i am generating N times rollouts to this weather and I am computing avarage distance as a heuristic to A* algorithm
# then in main i am calculating shortest path with A* algorithm, which use the heuristic received in _hopHeuristic() function from 10 samples(N)

import math
from random import random


class Graph:
    nodenames = []  # nodes names (position in table = node number)
    edges = []  # edges in form [number_node1, number_node_2, distance]

    def __init__(self, nodenames):
        self.nodenames = nodenames

    def getNodenames(self):
        return self.nodenames

    def addEdge(self, node1name, node2name, distance):
        self.edges.append([self.nodenames.index(node1name), self.nodenames.index(node2name), distance])

    def getNeighbours(self, node):
        neighbours = []
        for [n1, n2, d] in self.edges:
            if n1 == node: neighbours.append(n2)
            if n2 == node: neighbours.append(n1)
        return neighbours

    def getDist(self, node1, node2):
        for [n1, n2, d] in self.edges:
            if n1 == node1 and n2 == node2: return d
            if n2 == node1 and n1 == node2: return d
        return math.inf # return infinity if edge not found

    def dijkstraShortestPath(self, originName):
        # create vertex set Q
        q = list(range(len(self.nodenames)))  # [0,1,2,3…,len(nodes)]

        # for each vertex v in Graph:
        # dist[v] ← INFINITY
        # prev[v] ← UNDEFINED
        # add v to Q
        dist = [math.inf] * len(self.nodenames)
        prev = [None] * len(self.nodenames)

        # dist[source] ← 0
        dist[self.nodenames.index(originName)] = 0

        # while Q is not empty:
        while len(q) > 0:
            u = None
            # u ← vertex in Q with min dist[u]
            mindist = math.inf
            for qel in q:
                if dist[qel] < mindist:
                    mindist = dist[qel]
                    u = qel

            if u == None:  # cant find next vertex
                return dist, prev

            # remove u from Q
            q.remove(u)

            # for each neighbor v of u:
            for v in self.getNeighbours(u):
                # alt ← dist[u] + length(u, v)
                alt = dist[u] + self.getDist(u, v)
                # if alt < dist[v]:
                if alt < dist[v]:
                    # dist[v] ← alt
                    # prev[v] ← u
                    dist[v] = alt
                    prev[v] = u

        return dist, prev

    def __str__(self):
        s = ""
        for n in range(len(self.nodenames)):
            s += str(n) + " " + self.nodenames[n] + " : "
            for n2 in self.getNeighbours(n):
                s += str(n2) + "-" + self.nodenames[n2] + "-" + str(self.getDist(n, n2)) + "; "
            s += "\n"
        return s


class CanadianTravelerGraph(Graph):
    probableEdges = []  # edges in form [number_node1, number_node_2, distance, probability(treshold)]

    def addEdge(self, node1name, node2name, distance, p):
        self.probableEdges.append([self.nodenames.index(node1name), self.nodenames.index(node2name), distance, p])

    def sampleWeather(self):  # generates random edges based on problabilities (p==0 → edge always exist; p==1 → edge is blocked)
        self.edges = []
        for n1, n2, dist, p in self.probableEdges:
            if p <= random():  # random → [0,1)
                self.edges.append([n1, n2, dist])

    def bestWeather(self):  # generates edges ignoring weather
        self.edges = []
        for n1, n2, dist, p in self.probableEdges:
            self.edges.append([n1, n2, dist])

    def _hopHeuristic(self, origin, goal):
        N = 10  # 0
        i = N
        costsum = 0
        while i > 0:
            self.sampleWeather()
            #print(self)
            dist, prev = self.dijkstraShortestPath(self.nodenames[origin])
            #print(dist)
            #print(origin)

            if dist[goal] != math.inf:
                costsum += dist[goal]
                i -= 1

        # makes all edges unlocked

        return costsum / N

    def aStarHopShortestPath(self, originName, goalName):
        origin = self.nodenames.index(originName)
        goal = self.nodenames.index(goalName)

        # The set of nodes already evaluated
        visitedSet = []

        # The set of currently discovered nodes that are not evaluated yet.
        # Initially, only the start node is known.
        unvisitedSet = [origin]

        # For each node, which node it can most efficiently be reached from.
        # If a node can be reached from many nodes, stepfrom will eventually contain the
        # most efficient previous step.
        goFrom = [None] * len(self.nodenames)

        # For each node, the cost of getting from the start node to that node.
        gScore = [math.inf] * len(self.nodenames)

        # The cost of going from start to start is zero.
        gScore[origin] = 0

        # For each node, the total cost of getting from the start node to the goal
        # by passing by that node. That value is partly known, partly heuristic.
        finalScore = [math.inf] * len(self.nodenames)

        self.bestWeather()

        # For the first node, that value is completely heuristic.
        finalScore[origin] = self._hopHeuristic(origin, goal)



        while unvisitedSet != []:
            # the node in unvisited set having the lowest finalScore[] value

            minimumFinalScore = min([finalScore[o] for o in unvisitedSet])
            c_position = [o for o in unvisitedSet if finalScore[o] == minimumFinalScore][0]

            if c_position == goal:   #c_position -> current position
                return gScore, goFrom

                # return reconstruct_path(goFrom, c_position)

            unvisitedSet.remove(c_position)
            visitedSet.append(c_position)

            for neighbor in self.getNeighbours(c_position):
                if neighbor in visitedSet:
                    continue  # Ignore the neighbor which is already evaluated.

#                self.sampleWeather()

                # The distance from start to a neighbor
                test_gScore = gScore[c_position] + self.getDist(c_position, neighbor)

                if neighbor not in unvisitedSet:  # Discover a new node
                    unvisitedSet.append(neighbor)
                else:
                    if test_gScore >= gScore[neighbor]:
                        continue;

                # This path is the best until now. Record it!
                goFrom[neighbor] = c_position
                gScore[neighbor] = test_gScore
                finalScore[neighbor] = gScore[neighbor] + self._hopHeuristic(neighbor, goal)



# main class of the program
def main():
    g = CanadianTravelerGraph(
        ["Oradea", "Zerind", "Sibiu", "Arad", "Timisoara", "Lugoj", "Mehadia", "Dobreta", "Craiova", "Pitesti",
         "Bucharest", "Fagaras", "Giurgiu", "Urziceni", "Hirsova", "Vaslui", "Eforie", "Iasi", "Neamt", "R.Vilcea"])
    g.addEdge("Arad", "Sibiu", 140,         0)
    g.addEdge("Arad", "Timisoara", 118,     0.2)
    g.addEdge("Arad", "Zerind", 75,         0)
    g.addEdge("Bucharest", "Fagaras", 211,  0.1)
    g.addEdge("Bucharest", "Giurgiu", 90,   0.1)
    g.addEdge("Bucharest", "Pitesti", 101,  0.1)
    g.addEdge("Bucharest", "Urziceni", 85,  0)
    g.addEdge("Craiova", "Dobreta", 120,    0)
    g.addEdge("Craiova", "Pitesti", 138,    0)
    g.addEdge("Craiova", "R.Vilcea", 146,   0.1)
    g.addEdge("Dobreta", "Mehadia", 75,     0)
    g.addEdge("Eforie", "Hirsova", 86,      0.1)
    g.addEdge("Fagaras", "Sibiu", 99,       1)
    g.addEdge("Hirsova", "Urziceni", 98,    0.1)
    g.addEdge("Iasi", "Neamt", 87,          0)
    g.addEdge("Iasi", "Vaslui", 92,         0)
    g.addEdge("Lugoj", "Mehadia", 70,       0)
    g.addEdge("Lugoj", "Timisoara", 111,    0)
    g.addEdge("Oradea", "Sibiu", 151,       0)
    g.addEdge("Oradea", "Zerind", 71,       0)
    g.addEdge("Pitesti", "R.Vilcea", 97,    0.1)
    g.addEdge("R.Vilcea", "Sibiu", 80,      1)
    g.addEdge("Urziceni", "Vaslui", 142,    0)


    names = g.getNodenames()

    # g.sampleWeather()
    # print(g)
    #print(g._hopHeuristic(names.index("Arad"),names.index("Eforie")))
    #print(g._hopHeuristic(names.index("Fagaras"),names.index("Arad")))
    # return

    origin = "Neamt"
    originpos = names.index(origin)
    destination = "Arad"
    destinationpos = names.index(destination)
#    dist, prev = g.dijkstraShortestPath(origin)
    dist, prev = g.aStarHopShortestPath(origin, destination)



    if dist[destinationpos] == math.inf:
        print("Can't reach destination")
        print(dist)
        print(prev)
    else:
        print("shortest path:")
        nodepos = destinationpos
        while nodepos != originpos:
            p = prev[nodepos]
            print(names[nodepos] + " —" + str(g.getDist(nodepos, p)) + "— " + names[p])
            nodepos = p


if __name__ == "__main__":
    main()

