import uuid
import random
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors, font_color='white', font_size=10, width=2)
    plt.show()

def generate_color(index, total):
    intensity = int(100 * index / total)
    return f"#00{(55 + intensity * 2):2x}{(155 + intensity):02x}"

def dfs_memo(node, total):
    counter = 0
    def dfs(node, total = 0,  visited = []):
        nonlocal counter
        if node:
            node.color = generate_color(counter, total)
            counter += 1
            visited.append(node)
            dfs(node.left, total, visited)
            dfs(node.right, total, visited)
    
    dfs(node, total)

def bfs(root, total):
    queue = [root]
    index = 0
    visited = []
    while queue:
        node = queue.pop(0)
        node.color = generate_color(index, total)
        visited.append(node)
        index += 1
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

def build_tree(values):
    heap = [None]
    for val in values:
        heap.append(Node(val))

    for i in range(1, len(heap)):
        if 2*i < len(heap):
            heap[i].left = heap[2*i]
        if 2*i + 1 < len(heap):
            heap[i].right = heap[2*i + 1]
    
    return heap[1], len(values)

heap = [random.randint(1, 100) for _ in range(15)]

root, total = build_tree(heap)
dfs_memo(root, total)
draw_tree(root)

root, total = build_tree(heap)
bfs(root, total)
draw_tree(root)

