import heapq
# Define the number of vertices and edges
n = 15  # Number of vertices
m = 19  # Number of edges
# Define the adjacency list to represent the graph
adj = [[] for _ in range(n + 1)]

# Initialize the adjacency list
def initialize_map():
    adj[0].extend([(1, 35), (2, 40),(9,35),(10,35)])
    adj[1].extend([(2, 35), (12, 105),(0,35)])
    adj[2].extend([(1, 35), (3, 160), (0, 40)])
    adj[3].extend([(2, 160), (4, 90)])
    adj[4].extend([(3, 90), (5, 90)])
    adj[5].extend([(6, 65), (7, 35)])
    adj[6].extend([(5, 65), (7, 60),(8,70)])
    adj[7].extend([(5, 35), (6, 60),(13,85)])
    adj[8].extend([(6, 70), (14, 55), (15, 80)])
    adj[9].extend([(0,35)])
    adj[10].extend([(0,35)])
    adj[12].extend([(1,105), (13, 210)])
    adj[13].extend([ (12,210),(14,135)])
    adj[14].extend([ (13, 135),(8,55),(15,55)])
    adj[15].extend([(8,80),(14,55)])
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
# 00 bamm line 01 re phai 10 re trai 11 di thang
directions = [
    (0, 2, "00001110"),
    (0, 1, "00000110"),
    (0, 9, "00001110"),
    (1, 2, "00000110"),
    (1, 12, "00000010"),
    (2, 1, "00001010"),
    (2, 3, "00000010"),
    (2, 0, "00001110"), 
    (3, 4, "00000010"),
    (3, 2, "00001110"),
    (4, 3, "00000010"),
    (4, 5, "00000010"),
    (5, 7, "00000110"),
    (5, 6, "00001110"),
    (6, 7, "00001010"),
    (6, 5, "00001110"),
    (6, 8, "00001110"),
    (6, 13, "00000010"),
    (7, 5, "00001010"),
    (7, 6, "00000110"),
    (7, 13, "00001010"),
    (8, 6, "00001110"),
    (8, 15, "00001110"),
    (8, 14, "00000110"),
    (9, 0, "00001110"),
    (10, 0, "00000110"),
    (12, 1, "00001110"),
    (12, 13, "00000010"),
    (13, 12, "00001010"),
    (13,14, "00001000"),
    (14,13, "00001010"),
    (14,8, "00001010"),
    (14,15, "00000110"),
    (15,14, "00001010"),
    (15,8, "00001110")
    
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