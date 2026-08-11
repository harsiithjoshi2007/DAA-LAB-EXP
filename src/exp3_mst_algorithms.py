"""Experiment 3: Minimum Spanning Tree using Kruskal and Prim."""

from collections import defaultdict


def kruskal(graph):
    """Return MST cost using Kruskal's algorithm."""
    parent = {node: node for node in graph}
    rank = {node: 0 for node in graph}
    edges = []

    for u in graph:
        for v, w in graph[u]:
            if u < v:
                edges.append((w, u, v))

    edges.sort()
    mst_cost = 0
    mst_edges = []

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        rx, ry = find(x), find(y)
        if rx == ry:
            return False
        if rank[rx] < rank[ry]:
            parent[rx] = ry
        elif rank[rx] > rank[ry]:
            parent[ry] = rx
        else:
            parent[ry] = rx
            rank[rx] += 1
        return True

    for weight, u, v in edges:
        if union(u, v):
            mst_cost += weight
            mst_edges.append((u, v, weight))
            if len(mst_edges) == len(graph) - 1:
                break

    return mst_cost, mst_edges


def prim(graph):
    """Return MST cost using Prim's algorithm."""
    start = next(iter(graph))
    visited = {start}
    mst_cost = 0
    mst_edges = []
    edges = []

    for v, w in graph[start]:
        edges.append((w, start, v))

    while len(visited) < len(graph) and edges:
        edges.sort()
        weight, u, v = edges.pop(0)
        if v in visited:
            continue
        visited.add(v)
        mst_cost += weight
        mst_edges.append((u, v, weight))

        for neighbor, wt in graph[v]:
            if neighbor not in visited:
                edges.append((wt, v, neighbor))

    return mst_cost, mst_edges


def demo():
    graph = {
        'A': [('B', 2), ('C', 3)],
        'B': [('A', 2), ('C', 1), ('D', 4)],
        'C': [('A', 3), ('B', 1), ('D', 5)],
        'D': [('B', 4), ('C', 5)],
    }

    print("Experiment 3: Minimum Spanning Tree")
    print("Graph:", graph)

    kruskal_cost, kruskal_edges = kruskal(graph)
    prim_cost, prim_edges = prim(graph)

    print("Kruskal MST cost:", kruskal_cost)
    print("Kruskal edges:", kruskal_edges)
    print("Prim MST cost:", prim_cost)
    print("Prim edges:", prim_edges)


if __name__ == "__main__":
    demo()
