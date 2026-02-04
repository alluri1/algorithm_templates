from collections import deque

def main(grid):
    ROWS = len(grid)
    COLS = len(grid[0])
    visited = set()

    def dfs(i, j, visited):
        # base case - return out of bounds, in visited
        if i < 0 or i >= ROWS or j < 0 or j >= COLS or (i, j) in visited:
            return False
        visited.add((i, j))

        # recurse on neighbors
        dfs(i - 1, j, visited)
        dfs(i + 1, j, visited)
        dfs(i, j - 1, visited)
        dfs(i, j + 1, visited)

    for r in range(ROWS):
        for c in range(COLS):
            if (r, c) not in visited:
                dfs(r, c, visited)


def main_bfs(matrix) :
    # Check if input is empty
    if not matrix or not matrix[0]:
        return []

    num_rows, num_cols = len(matrix), len(matrix[0])

    # Setup each queue with cells adjacent to their respective ocean
    pacific_queue = deque()
    for i in range(num_rows):
        pacific_queue.append((i, 0))


    def bfs(queue):
        visited = set()
        while queue:
            (row, col) = queue.popleft()
            # This cell is visited, so mark it
            visited.add((row, col))
            for (x, y) in [(1, 0), (0, 1), (-1, 0), (0, -1)]: # Check all 4 directions
                new_row, new_col = row + x, col + y
                # Check if the new cell is within bounds
                if new_row < 0 or new_row >= num_rows or new_col < 0 or new_col >= num_cols:
                    continue
                # Check that the new cell hasn't already been visited
                if (new_row, new_col) in visited:
                    continue
                # If we've gotten this far, that means the new cell is visited
                queue.append((new_row, new_col))
        return visited

    # Perform a BFS for each ocean to find all cells accessible by each ocean
    pacific_reachable = bfs(pacific_queue)

    return pacific_reachable
