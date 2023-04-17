import numpy as np

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = np.zeros((self.V, self.V))

    def add_edge(self, u, v, w):
        self.graph[u][v] = w
        self.graph[v][u] = w

    def boruvka(self):
        parent = [-1] * self.V
        rank = [0] * self.V
        cheapest = [-1] * self.V
        subsets = []
        for i in range(self.V):
            subsets.append([i, 0])
        num_trees = self.V
        while num_trees > 1:
            for i in range(self.V):
                cheapest[i] = -1
            for i in range(self.V):
                for j in range(self.V):
                    if self.graph[i][j] != 0:
                        set1 = self.find(subsets, i)
                        set2 = self.find(subsets, j)
                        if set1 != set2:
                            if cheapest[set1] == -1 or self.graph[i][j] < self.graph[cheapest[set1][0]][cheapest[set1][1]]:
                                cheapest[set1] = [i, j]
                            if cheapest[set2] == -1 or self.graph[i][j] < self.graph[cheapest[set2][0]][cheapest[set2][1]]:
                                cheapest[set2] = [i, j]
            for i in range(self.V):
                if cheapest[i] != -1:
                    set1 = self.find(subsets, cheapest[i][0])
                    set2 = self.find(subsets, cheapest[i][1])
                    if set1 != set2:
                        if rank[set1] > rank[set2]:
                            parent[set2] = set1
                        elif rank[set1] < rank[set2]:
                            parent[set1] = set2
                        else:
                            parent[set2] = set1
                            rank[set1] += 1
                        num_trees -= 1
        for i in range(self.V):
            if parent[i] != -1:
                print(parent[i], "-", i, "\t", self.graph[i][parent[i]])

    def find(self, subsets, i):
        if subsets[i][0] != i:
            subsets[i][0] = self.find(subsets, subsets[i][0])
        return subsets[i][0]


# Зчитуємо граф з файлу
with open('graph_3.txt', 'r') as f:
    lines = f.readlines()
    V = len(lines)
    g = Graph(V)
    for i in range(V):
        row = list(map(int, lines[i].strip().split()))
        for j in range(V):
            if row[j] != 0:
                g.add_edge(i, j, row[j])

# Викликаємо метод для побудови мінімального остовного дерева
g.boruvka()
