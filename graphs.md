# Graphs

## Undirected Graphs

### Eulerian Path
 - Eulerian path: a path in graph that visits every edge exactly once

### Eulerian Cycle 
1. All vertices with non-zero degree are connected. We don’t care about vertices with zero degree because they don’t belong to Eulerian Cycle or Path (we only consider all edges).
2. All vertices have even degree.


### Eulerian Path
1. Same as condition (1) for Eulerian Cycle
2. If two vertices have odd degree and all other vertices have even degree. Note that only one vertex with odd degree is not possible in an undirected graph (sum of all degrees is always even in an undirected graph)

*Note that a graph with no edges is considered Eulerian because there are no edges to traverse.*

### Hierholzer’s Algorithm for directed graph
O(E) where E is number of edges; i.e. linear time 
- Choose any starting vertex v, and follow a trail of edges from that vertex until returning to v. It is not possible to get stuck at any vertex other than v, because indegree and outdegree of every vertex must be same, when the trail enters another vertex w there must be an unused edge leaving w.
The tour formed in this way is a closed tour, but may not cover all the vertices and edges of the initial graph.
- As long as there exists a vertex u that belongs to the current tour but that has adjacent edges not part of the tour, start another trail from u, following unused edges until returning to u, and join the tour formed in this way to the previous tour.

Thus the idea is to keep following unused edges and removing them until we get stuck. Once we get stuck, we back-track to the nearest vertex in our current path that has unused edges, and we repeat the process until all the edges have been used. We can use another container to maintain the final path.

**See [find itinerary](https://leetcode.com/problems/reconstruct-itinerary/) on leetcode or in examples/find-itinerary**
