# Function to implement recursive AO* Algorithm
def recAOStar(n):
    global finalPath
    print("Expanding Node : ", n)

    and_nodes = []  # List to store AND nodes
    or_nodes = []   # List to store OR nodes

    # Segregation of AND and OR nodes
    if n in allNodes:
        if 'AND' in allNodes[n]:
            and_nodes = allNodes[n]['AND']
        if 'OR' in allNodes[n]:
            or_nodes = allNodes[n]['OR']

    # If leaf node then return
    if len(and_nodes) == 0 and len(or_nodes) == 0:
        return

    solvable = False
    marked = {}

    # Main loop to explore the graph
    while not solvable:
        # If all child nodes are visited, take the least cost of all child nodes
        if len(marked) == len(and_nodes) + len(or_nodes):
            min_cost_least, min_cost_group_least = least_cost_group(and_nodes, or_nodes, {})
            solvable = True
            change_heuristic(n, min_cost_least)
            optimal_child_group[n] = min_cost_group_least
            continue

        # Calculate least cost of unmarked child nodes
        min_cost, min_cost_group = least_cost_group(and_nodes, or_nodes, marked)
        is_expanded = False

        # Recursively visit child nodes if they have subtrees
        for child in min_cost_group:
            if child in allNodes:
                is_expanded = True
                recAOStar(child)

        # Update heuristic if the child node was expanded
        if is_expanded:
            min_cost_verify, min_cost_group_verify = least_cost_group(and_nodes, or_nodes, {})
            if min_cost_group == min_cost_group_verify:
                solvable = True
                change_heuristic(n, min_cost_verify)
                optimal_child_group[n] = min_cost_group
        else:
            # Update min cost of current node if no subtree
            solvable = True
            change_heuristic(n, min_cost)
            optimal_child_group[n] = min_cost_group

        # Mark the expanded child node
        marked[min_cost_group] = 1

    return heuristic(n)

# Function to calculate the min cost among all child nodes
def least_cost_group(and_nodes, or_nodes, marked):
    node_wise_cost = {}
    
    # Calculate cost for AND nodes
    for node_pair in and_nodes:
        if not node_pair[0] + node_pair[1] in marked:
            cost = heuristic(node_pair[0]) + heuristic(node_pair[1]) + 2
            node_wise_cost[node_pair[0] + node_pair[1]] = cost

    # Calculate cost for OR nodes
    for node in or_nodes:
        if not node in marked:
            cost = heuristic(node) + 1
            node_wise_cost[node] = cost

    min_cost = 999999
    min_cost_group = None

    # Find node group with minimum heuristic
    for costKey in node_wise_cost:
        if node_wise_cost[costKey] < min_cost:
            min_cost = node_wise_cost[costKey]
            min_cost_group = costKey

    return [min_cost, min_cost_group]

# Returns heuristic of a node
def heuristic(n):
    return H_dist[n]

# Updates the heuristic of a node
def change_heuristic(n, cost):
    H_dist[n] = cost

# Function to print the optimal cost nodes
def print_path(node):
    print(optimal_child_group[node], end="")
    node = optimal_child_group[node]

    # Recursively print the path
    for child in node:
        if child in optimal_child_group:
            print("->", end="")
            print_path(child)

# Define the heuristic values here
H_dist = { 'A': -1,'B': 4, 'C': 2, 'D': 3, 'E': 6,'F': 8, 'G': 2,'H': 0, 'I': 0, 'J': 0}

# Define your graph here
allNodes = {
'A': {'AND': [('C', 'D')], 'OR': ['B']},
'B': {'OR': ['E', 'F']},
'C': {'OR': ['G'], 'AND': [('H', 'I')]},
'D': {'OR': ['J']}
}


# Initialize a dictionary to keep track of optimal child groups
optimal_child_group = {}

# Execute the algorithm starting from node 'A'
optimal_cost = recAOStar('A')
print('Nodes which gives optimal cost are')
print_path('A')
print('\nOptimal Cost is :: ', optimal_cost)
