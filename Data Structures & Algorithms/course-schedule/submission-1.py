class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = [[] for _ in range(numCourses)]
        for src, dst in prerequisites:
            adjList[src].append(dst)

        indegree = [0] * (numCourses)
        for i in range(len(adjList)):
            for next_node in adjList[i]:
                indegree[next_node] += 1
        
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            node = queue.popleft()
            for next_node in adjList[node]:
                indegree[next_node] -= 1
                if indegree[next_node] == 0:
                    queue.append(next_node)
        
        for i in indegree:
            if i != 0:
                return False
        return True
        

        
