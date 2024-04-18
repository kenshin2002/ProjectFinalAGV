import heapq
# Define the number of vertices and edges
n = 15  # Number of vertices
m = 19  # Number of edges
# Define the adjacency list to represent the graph
adj = [[] for _ in range(n + 1)]

# Initialize the adjacency list
def initialize_map():
    adj[1].extend([(2, 150), (12, 30)])
    adj[2].extend([(1, 150), (3, 65), (14, 35)])
    adj[3].extend([(2, 65), (6, 70), (14, 60)])
    adj[4].extend([(9, 105), (7, 210)])
    adj[5].extend([(12, 160), (11, 40)])
    adj[6].extend([(3, 70), (13, 80),(8, 55)])
    adj[7].extend([(14, 85), (4, 210), (8, 135)])
    adj[8].extend([(6, 55), (13, 55), (7, 135)])
    adj[9].extend([(5,35), (4, 105), (11, 35)])
    adj[10].extend([(11,35)])
    adj[11].extend([(10,35), (5, 40), (9, 35),(15,30)])
    adj[12].extend([(1,30), (5, 160)])
    adj[13].extend([(6,80), (8,55)])
    adj[14].extend([ (7, 85)])
    adj[15].extend([(11,30)])
# Dijkstra's Algorithm
def dijkstra(s, t):
    INF = float('inf')
    d = [INF] * (n + 1)
    pre = [0] * (n + 1)
    d[s] = 0

    pq = [(0, s)]

    while pq:
        dist_u, u = heapq.heappop(pq)
        if dist_u > d[u]:
            continue
        for v, w in adj[u]:
            if d[v] > d[u] + w:
                d[v] = d[u] + w
                pre[v] = u
                heapq.heappush(pq, (d[v], v))

    path = []
    while t != s:
        path.append(t)
        t = pre[t]
    path.append(s)
    path.reverse()
    return path

# Define directions
directions = [
    (1, 2, "00000010"),
    (1, 12, "00000010"),
    (2, 1, "00000010"),
    (2, 3, "00000010"),
    (2, 14, "00000101"), 
    (3, 4, "00000010"),
    (3, 6, "00000010"),
    (3, 14, "00001001"),
    (4, 8, "00000010"),
    (4, 9, "00000010"),
    (4, 7, "00001001"),
    (5, 12, "00000010"),
    (5, 11, "00000010"),
    (6, 3, "00000010"),
    (6, 8, "00000101"),
    (6, 13, "00000010"),
    (7, 4, "00001001"),
    (7, 14, "00000101"),
    (7, 8, "00000101"),
    (8, 6, "00001001"),
    (8, 7, "00000010"),
    (8, 13, "00000101"),
    (9, 4, "00000010"),
    (9, 5, "00000101"),
    (9, 11, "00001001"),
    (10, 11, "00000101"),
    (11, 9, "00000101"),
    (11,5, "00000010"),
    (11,15, "00000010"),
    (12,1, "00000010"),
    (12,5, "00000010"),
    (13,6, "00000010"),
    (13,8, "00001001"),
    
    
    (14,7, "00001001"),
    (15,11,"00000010")
]

# Create a route based on the path and directions
def create_route(path, directions):
    route = ""
    for i in range(len(path) - 1):
        from_node, to_node = path[i], path[i + 1]
        for dir_from, dir_to, direction in directions:
            if from_node == dir_from and to_node == dir_to:
                route += f"{from_node}_{direction}_"
                break
    route += f"{path[-1]}_00000000"
    return route

initialize_map()