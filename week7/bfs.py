import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


class Graph:
    def __init__(self):
        self.graph = nx.Graph()

    def add_edge(self, start, end):
        self.graph.add_edge(start, end)

    def bfs(self, start, target):
        visited = set()
        queue = deque([(start, [start])])
        visited.add(start)

        while queue:
            node, path = queue.popleft()

            if node == target:
                return path

            # Prioritize neighbors closer to the target based on heuristic
            neighbors = sorted(self.graph[node], key=lambda x: self.heuristic(x, target))

            for neighbor in neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))

        return None

    def heuristic(self, node, target):
        # Simple heuristic example: Euclidean distance if nodes have coordinates.
        # Here, assume nodes are tuples representing coordinates.
        return ((node[0] - target[0]) ** 2 + (node[1] - target[1]) ** 2) ** 0.5

    def draw_graph(self, path=None):
        pos = {node: node for node in self.graph.nodes()}  # Using node values as positions
        nx.draw(self.graph, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=500,
                font_size=10)

        if path:
            edges_in_path = list(zip(path, path[1:]))
            nx.draw_networkx_edges(self.graph, pos, edgelist=edges_in_path, edge_color='red', width=2)
            nx.draw_networkx_nodes(self.graph, pos, nodelist=path, node_color='red')

        plt.show()


# Example usage:
graph = Graph()

# Adding edges for a complex graph
edges = [
    ((0, 0), (1, 0)),
    ((0, 0), (0, 1)),
    ((1, 0), (1, 1)),
    ((0, 1), (1, 1)),
    ((1, 1), (2, 1)),
    ((2, 1), (2, 2)),
    ((1, 1), (1, 2)),
    ((1, 2), (2, 2)),
    ((2, 2), (3, 2)),
    ((3, 2), (3, 3)),
    ((3, 3), (4, 3)),
    ((4, 3), (4, 4)),
    ((3, 3), (2, 3)),
    ((2, 3), (1, 3)),
    ((1, 3), (0, 3)),
    ((0, 3), (0, 2)),
    ((0, 2), (1, 2)),
    ((0, 2), (0, 1)),
    ((3, 2), (3, 1)),
    ((3, 1), (2, 1)),
]

for edge in edges:
    graph.add_edge(*edge)

start = (0, 0)
target = (4, 4)

path = graph.bfs(start, target)
print(f"Path from {start} to {target}: {path}")

# Draw the graph with the path highlighted
graph.draw_graph(path)
