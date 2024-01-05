# Function to implement A* Search Algorithm
def A_star(start_node, stop_node):
    # Initialize open and closed sets
    open_set = set(start_node)
    closed_set = set()

    # g stores the distance from the starting node
    g = {}

    # parents contains an adjacency map of all nodes
    parents = {}

    # Distance of the starting node from itself is zero
    g[start_node] = 0

    # start_node is the root node and hence its parent is set to itself
    parents[start_node] = start_node

    # Loop until there are nodes to be evaluated
    while len(open_set) > 0:
        n = None

        # Find the node with the lowest value of f()
        for v in open_set:
            if n == None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v

        # Check if we have reached the stop_node or if the next node is None
        if n == stop_node or Graph_nodes[n] == None:
            # skip the rest of the loop
            pass
        else:
            # Explore neighbors
            for (m, weight) in get_neighbors(n):
                # Add unvisited neighbors to the open set
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    parents[m] = n  # Set parent
                    g[m] = g[n] + weight  # Update distance

                # Check if a better path exists through the current node
                elif g[m] > g[n] + weight:
                    g[m] = g[n] + weight  # Update the distance
                    parents[m] = n  # Update the parent

                    # If it's in the closed set, move it to open set
                    if m in closed_set:
                        closed_set.remove(m)
                        open_set.add(m)

        # If no node is left to explore, return None
        if n == None:
            print('Path does not exist!')
            return None

        # If the stop node is reached, reconstruct the path
        if n == stop_node:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start_node)
            path.reverse()

            print('Optimal Path :')
            return path

        # Move the node from open to closed set after exploring
        open_set.remove(n)
        closed_set.add(n)

    # If the path is not found
    print('Path does not exist!')
    return None

# Function to return neighbors and their distances from a node
def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return None

# Function to return heuristic distance for all nodes
def heuristic(n):
    H_dist = {
        'S': 8, 'A': 8, 'B': 4, 'C': 3,
        'D': 1000, 'E': 1000, 'G': 0,
    }
    return H_dist[n]

# Define the graph
Graph_nodes = {
    'S': [['A', 1], ['B', 5], ['C', 8]],
    'A': [['D', 3], ['E', 7], ['G', 9]],
    'B': [['G', 4]],
    'C': [['G', 5]],
    'D': None,
    'E': None
}

# Execute the algorithm
A_star('S', 'G')
