# Розробіть алгоритм Дейкстри для знаходження найкоротших шляхів у зваженому графі, використовуючи бінарну купу. 
# Завдання включає створення графа, використання піраміди для оптимізації вибору вершин та обчислення найкоротших шляхів від початкової вершини до всіх інших.

import heapq
import networkx as nx

def dijkstra(graph, start):
    queue = [(0, start)]
    visited = set()
    distances = {start: 0}
    while queue:
        (cost, node) = heapq.heappop(queue)
        if node in visited:
            continue
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor in visited:
                continue
            new_cost = cost + graph[node][neighbor]['weight']
            if neighbor not in distances or new_cost < distances[neighbor]:
                distances[neighbor] = new_cost
                heapq.heappush(queue, (new_cost, neighbor))
    return distances

G = nx.Graph()
G.graph['name'] = '11 Biggest Cities of Netherlands'

G.add_edge('Amsterdam', 'Utrecht', weight=45)
G.add_edge('Amsterdam', 'The Hague', weight=65)
G.add_edge('Rotterdam', 'Utrecht', weight=62)
G.add_edge('Rotterdam', 'The Hague', weight=24)
G.add_edge('Amsterdam', 'Zwolle', weight=103)
G.add_edge('Utrecht', 'Zwolle', weight=90)
G.add_edge('Utrecht', 'Arnhem', weight=65)
G.add_edge('Nijmegen', 'Arnhem', weight=19)
G.add_edge('Arnhem', 'Zwolle', weight=67)
G.add_edge('Nijmegen', 'Eindhoven', weight=73)
G.add_edge('Maastricht', 'Eindhoven', weight=88)
G.add_edge('Maastricht', 'Nijmegen', weight=140)
G.add_edge('Eindhoven', 'Rotterdam', weight=111)
G.add_edge('Amsterdam', 'Leeuwarden', weight=140)
G.add_edge('Leeuwarden', 'Groningen', weight=60)
G.add_edge('Groningen', 'Zwolle', weight=106)

distances = dijkstra(G, 'Maastricht')
for city, distance in distances.items():
    print(f"Distance from Amsterdam to {city}: {distance}")
