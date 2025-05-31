# Function to find BFS of Graph from given source s

# 인접 리스트로 표현한 2차원 리스트 사용
def bfs(adj):

    # get number of vertices
    V = len(adj)

    # create an array to store the traversal
    res = []
    s = 0 # 시작 정점
    # Create a queue for BFS
    from collections import deque
    q = deque()

    # Initially mark all the vertices as not visited
    visited = [False] * V

    # Mark source node as visted and enqueue it
    visited[s] = True
    q.append(s) # 시작 정점 방문 처리

    # Iterate over the queue
    while q:

        # Dequeue a vertex from queue and store it
        curr = q.popleft() # current vertex
        res.append(curr)

        # Get all adjacent vertices of the dequeued
        # vertex curr If an adjacent has not been
        # visited, mark it visited and enqueue it
        for x in adj[curr]:
            if not visited[x]:
                visited[x] = True
                q.append(x)

    return res

if __name__ == "__main__":

    # create the adjacency list
    # [ [2, 3, 1], [0], [0, 4], [0], [2] ]
    adj = [[1, 2], [0, 2, 3], [0, 4], [1, 4], [2, 3]]
    ans = bfs(adj)

    print(" ".join(map(str, ans)))