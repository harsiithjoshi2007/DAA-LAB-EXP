"""Experiment 4: Dijkstra's Shortest Path algorithm."""

import heapq


def dijkstra(graph, start):
    """Compute shortest paths from a source using Dijkstra's algorithm."""
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    path = {start: [start]}

    while priority_queue:
        current_distance, node = heapq.heappop(priority_queue)

        if current_distance > distances[node]:
            continue

        for neighbor, weight in graph[node]:
            new_distance = current_distance + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                path[neighbor] = path[node] + [neighbor]
                heapq.heappush(priority_queue, (new_distance, neighbor))

    return distances, path


def demo():
    graph = {
        'A': [('B', 4), ('C', 2)],
        'B': [('A', 4), ('C', 3), ('D', 2)],
        'C': [('A', 2), ('B', 3), ('D', 1), ('E', 5)],
        'D': [('B', 2), ('C', 1), ('E', 4)],
        'E': [('C', 5), ('D', 4)],
    }

    source = 'A'
    distances, paths = dijkstra(graph, source)

    print("Experiment 4: Dijkstra's Shortest Path")
    print("Source:", source)
    print("Shortest distances:", distances)
    print("Paths:", paths)


if __name__ == "__main__":
    demo()
