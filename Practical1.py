from collections import deque

def bfs(graph, start):
    visited = set()                  # To keep track of visited nodes
    queue = deque([start])          # Initialize queue with start node

    print("BFS Traversal:", end=" ")

    while queue:
        vertex = queue.popleft()    # Dequeue a node

        if vertex not in visited:
            print(vertex, end=" ")  # Process the node
            visited.add(vertex)     # Mark as visited

            # Enqueue unvisited neighbors
            for neighbor in graph.get(vertex, []):
                if neighbor not in visited:
                    queue.append(neighbor)

# Example Graph represented as adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Run BFS
bfs(graph, 'A')
