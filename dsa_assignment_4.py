#1Q Breadth First Traversal for a Graph

from collections import deque
class graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, v, u):
        if v in self.graph:
            self.graph[v].append(u)
        else:
            self.graph[v] = [u]
    def breadth_first_traversal(self, start_vertex):
      visited = set()
      queue = deque([start_vertex])
      while queue:
         vertex = queue.popleft()
         if vertex not in visited:
                print(vertex, end=' ')
                visited.add(vertex)
                if vertex in self.graph:
                    for neighbor in self.graph[vertex]:
                        if neighbor not in visited:
                            queue.append(neighbor)
g = graph()
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,2)
g.add_edge(2,0)
g.add_edge(2,3)
g.add_edge(3,3)
start_vertex = int(input('enter the vertex: '))
print('breadth of first traversal (starting from index)', start_vertex,"):")
g.breadth_first_traversal(start_vertex)


#2Q  Depth First Traversal for a Graph

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, v, u):
        if v in self.graph:
            self.graph[v].append(u)
        else:
            self.graph[v] = [u]

    def depth_first_traversal(self, start_vertex):
        visited = set()
        self._depth_first_traversal_helper(start_vertex, visited)

    def _depth_first_traversal_helper(self, vertex, visited):
        visited.add(vertex)
        print(vertex, end=' ')
        
        if vertex in self.graph:
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    self._depth_first_traversal_helper(neighbor, visited)
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

start_vertex = int(input('enter the vertex: '))
print("depth first traversal (starting from vertex", start_vertex,"):")
g.depth_first_traversal(start_vertex)


#3Q Count the number of nodes at given level in a tree using BFS

from collections import deque
adj = [[] for i in range(1001)]
def addEdge(v, w):     
    adj[v].append(w)
    adj[w].append(v)
def BFS(s, l):     
    V = 100     
    visited = [False] * V
    level = [0] * V
    for i in range(V):
        visited[i] = False
        level[i] = 0
    # Create a queue for BFS
    queue = deque()
    visited[s] = True
    queue.append(s)
    level[s] = 0
    while (len(queue) > 0):    
        s = queue.popleft()
        for i in adj[s]:
            if (not visited[i]):
                level[i] = level[s] + 1
                visited[i] = True
                queue.append(i)
    count = 0
    for i in range(V):
        if (level[i] == l):
            count += 1       
    return count
  
# Driver code
if __name__ == '__main__':
    addEdge(0, 1)
    addEdge(0, 2)
    addEdge(1, 3)
    addEdge(2, 4)
    addEdge(2, 5)
  
    level = int(input())
  
    print(BFS(0, level))


#4q Count number of trees in a forest

def addEdge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)
def dfsutil(u, adj, visited):
    visited[u] = True
    for i in range(len(adj[u])):
        if (visited[adj[u][i]] == False):
            dfsutil(adj[u][i], adj, visited)
def countTrees(adj, V):
    visited = [False] * V
    res = 0
    for u in range(V):
        if (visited[u] == False):
            dfsutil(u, adj, visited)
            res += 1
    return res

# Driver code
if __name__ == '__main__':
 
    V = 5
    adj = [[] for i in range(V)]
    addEdge(adj, 0, 1)
    addEdge(adj, 0, 2)
    addEdge(adj, 3, 4)
    print(countTrees(adj, V))


#5Q Detect Cycle in a Directed Graph

from collections import defaultdict
 
class Graph():
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices
    def addEdge(self, u, v):
        self.graph[u].append(v)
    def isCyclicUtil(self, v, visited, recStack):
        visited[v] = True
        recStack[v] = True
        for neighbour in self.graph[v]:
            if visited[neighbour] == False:
                if self.isCyclicUtil(neighbour, visited, recStack) == True:
                    return True
            elif recStack[neighbour] == True:
                return True
        recStack[v] = False
        return False
    def isCyclic(self):
        visited = [False] * (self.V + 1)
        recStack = [False] * (self.V + 1)
        for node in range(self.V):
            if visited[node] == False:
                if self.isCyclicUtil(node, visited, recStack) == True:
                    return True
        return False
 
# Driver code
if __name__ == '__main__':
    g = Graph(4)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
 
    if g.isCyclic() == 1:
        print("Graph contains cycle")
    else:
        print("Graph doesn't contain cycle")


# Below question is a miscellaneous question

# **Implement n-Queen’s Problem

def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True

def solve_n_queens(n):
    board = [['.' for _ in range(n)] for _ in range(n)]
    solutions = []

    def backtrack(row):
        if row == n:
            solutions.append([''.join(row) for row in board])
        else:
            for col in range(n):
                if is_safe(board, row, col, n):
                    board[row][col] = 'Q'
                    backtrack(row + 1)
                    board[row][col] = '.'
    backtrack(0)
    return solutions
n = 4
solutions = solve_n_queens(n)
for solution in solutions:
    for row in solution:
        print(row)
    print()