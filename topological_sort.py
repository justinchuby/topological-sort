from typing import List


def topological_sort(next_nodes: List[List[int]]):
    """Sort the graph with topological sort algorithm.

    Args:
        next_nodes: A list of lists, where each list contains the nodes that are
            connected to the node at the same index.
    """
    n = len(next_nodes)
    if n == 1:
        return [0]

    degree = [0 for _ in range(n)]
    output = []

    for node in range(n):
        for nextNode in next_nodes[node]:
            degree[nextNode] += 1

    for node in range(n):
        if degree[node] == 0:
            degree = current_path_extreme(node, next_nodes, degree, output, 0)

    return output

def current_path_extreme(node, next_nodes, degree, output: List[int], i: int):
    output.append(node)

    for next_node in next_nodes[node]:
        degree[next_node] -= 1
        if degree[next_node] == 0:
            degree[next_node] = -1
            degree = current_path_extreme(next_node, next_nodes, degree, output, i + 1)
    return degree


def test():
    nodes = [[1, 6, 8], [4, 2], [3], [8], [5], [3], [7], [8], [9], []]
    result = topological_sort(nodes)
    print(result)

test()
