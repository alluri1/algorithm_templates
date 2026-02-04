from collections import deque

# BFS from source
# prints only those vertices that are reachable from the source and
# would not print all vertices in case of disconnected graph
def bfs(adj_list, source):
    q = deque()
    q.append(source)
    V = len(adj_list)
    visited = [False]*V
    output = []
    while q:
        curr = q.popleft()
        output.append(curr)
        for neighbor in adj_list:
            if not visited[neighbor]:
                visited[neighbor] = True
                q.append(neighbor)
    return output

def bfsOfGraph(adj, s, visited, res):
    # Create a queue for BFS
    q = deque()

    # Mark source node as visited and enqueue it
    visited[s] = True
    q.append(s)

    # Iterate over the queue
    while q:

        # Dequeue a vertex and store it
        curr = q.popleft()
        res.append(curr)

        # Get all adjacent vertices of the dequeued
        # vertex curr If an adjacent has not been
        # visited, mark it visited and enqueue it
        for x in adj[curr]:
            if not visited[x]:
                visited[x] = True
                q.append(x)
    return res

# Perform BFS for the entire graph which maybe
# disconnected
def bfsDisconnected(adj):
    V = len(adj)

    # create an array to store the traversal
    res = []

    # Initially mark all the vertices as not visited
    visited = [False] * V

    # perform BFS for each node
    for i in range(V):
        if not visited[i]:
            bfsOfGraph(adj, i, visited, res)
    return res
