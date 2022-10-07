# Canadian-Traveller-Problem
The algorithms in Python for resolving Canadian Traveller Problem (CTP). CTP is a problem where the main goal is to find the shortest path between 2 nodes under uncertain conditions. The edges between nodes (roads) may be blocked, with a given probability. For this purpose 3 types of algorithms have been created:
- Optimism (OMT):

- Hindsight Optimization (HOP):
-
- Optimistic UCT (UCTO):

Strategy:
1. Choose an origin and destination nodes
2. Set the number of rollouts (N)
3. Add starting node to the belief sequence
4. Add the next node, which has the lowest distance cost to the belief sequence.
5. Repeat step 4 until destination.
6. Using belief sequence, compute shortest path.
