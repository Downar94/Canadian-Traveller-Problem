# Canadian-Traveller-Problem
## Description
The algorithms in Python for resolving Canadian Traveller Problem (CTP). CTP is a problem where the main goal is to find the shortest path between 2 nodes under uncertain conditions. The edges between nodes (roads) may be blocked, with a given probability. For this purpose 3 types of algorithms have been created:
### Optimism (OMT)

#### Strategy:
1. Find deterministic shortest path
2. 
### Hindsight Optimization (HOP)

#### Strategy:
1. Choose an origin and destination nodes
2. Set the number of rollouts (N)
3. Generate the weather at the rollout, according to the blockage probability. Now we have only blocked and traversable edges.
4. Find shortest path in each rollout to estimate travel cost and determine next action.
5. Calculate shortest path for the whole graph (the graph without blocked edges).

### Optimistic UCT (UCTO)

#### Strategy:
1. Choose an origin and destination nodes
2. Set the number of rollouts (N)
3. Add starting node to the belief sequence
4. Add the next node, which has the lowest distance cost to the belief sequence.
5. Repeat step 4 until destination.
6. Using belief sequence, compute shortest path.

## Results
### Hindsight Optimization (HOP)
### Optimistic UCT (UCTO)
Finding shortest path from Arad to Bucharest
#### Shortest path:
![shorterUCTO](https://user-images.githubusercontent.com/44844566/196765384-3477c6c9-6c07-4542-b447-ad25dd5b2e20.PNG)
![sampleFileName3](https://user-images.githubusercontent.com/44844566/196765382-89bd4ad9-9cd6-4818-8317-07705caf8ed6.png)
#### Longer path after R.Vilcea - Sibiu Edge blockage:
![largerUCTO](https://user-images.githubusercontent.com/44844566/196765387-94c54114-b33f-42ad-8e18-2db322992511.PNG)
![sampleFileName2](https://user-images.githubusercontent.com/44844566/196765377-57ac0297-e702-435d-9ac0-cd06613ad9c8.png)
### Optimism (OMT)
