from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, vertex, visited):
        visited.add(vertex)
        print(vertex, end=" ")

        for i in self.graph[vertex]:
            if i not in visited:
                visited.add(i)
                self.DFSUtil(i, visited)

    def DFS(self, vertex):
        visited = set()
        self.DFSUtil(vertex, visited)


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Following is DFS from (starting from vertex 2)")
g.DFS(2)

