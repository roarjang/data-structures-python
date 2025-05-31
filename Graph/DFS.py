# DFS(Depth First Search, 깊이 우선 탐색)
# 인접 행렬(adjacency matrix) 사용

def dfsRec(adj, visited, s, res):
	visited[s] = True # 현재 노드 방문 처리
	res.append(s) # 방문 순서에 추가
	
	# Recursively visit all adjacent vertices that are not visied yet
	for i in range(len(adj)):
		if adj[s][i] == 1 and not visited[i]: # 간선 존재 + 아직 방문하지 않았으면
			dfsRec(adj, visited, i, res) # 재귀 호출

def DFS(adj):
	visited = [False] * len(adj) # 모든 노드 방문 초기화
	res = [] # 결과 리스트
	dfsRec(adj, visited, 0, res) # Start DFS from vertex 0
	return res
	
def add_edge(adj, s, t):
	adj[s][t] = 1
	adj[t][s] = 1 # Since it's an undirected graph
	
# Driver code
V = 5
adj = [[0] * V for _ in range(V)] # Adjacency matrix (5x5 인접 행렬)

# Define the edges of the graph
edges = [(1, 2), (1, 0), (2, 0), (2, 3), (2, 4)]

# Populate the adjacency matrix with edges
for s, t in edges:
	add_edge(adj, s, t)
	
res = DFS(adj) # Perform DFS
print(" ".join(map(str, res)))