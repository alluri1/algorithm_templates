def dfs_rec(adj, visited, s):
    visited[s] = True
    for neighbor in adj[s]:
        if not visited[neighbor]:
            dfs_rec(adj, visited, neighbor)

def dfs(adj, source):
    visited = [False] * len(adj)
    dfs_rec(adj, visited, source)
