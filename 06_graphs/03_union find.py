class UnionFind:
    def __init__(self, size):
        # initialize with parent[i]= i
        self.parent = list(range(size))

    # Find the root of tree x belongs to
    # Recursively follows parent pointers until reaching root (where parent[root] = root).
    # Path compression: On return, sets each node along the path to point directly to root, flattening the tree for future finds.
    # Why it works: Path compression ensures most nodes have depth 1 after a few operations, dominating any imbalance from simple linking.
    #TC: O(log N), SC: O(N)
    def find(self, x):
        if self.parent[x] != x:
            return self.find(self.parent[x])  # Path compression
        else:
            return x

    # combines the groups containing x and y
    # set y subtree as child of x  subtree
    # TC: O(log N), SC: O(N)
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.parent[rootY] = rootX  # Simple link: y's root → x's root

    def connected(self, x, y):
        return self.find(x) == self.find(y)
