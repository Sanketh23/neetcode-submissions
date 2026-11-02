class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for source, dest in prerequisites:
            adjList[source].append(dest)
            indegree[dest] += 1

        queue = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            node = queue.popleft()
            for neighbor in adjList[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        for ind in indegree:
            if ind != 0:
                return False
        return True
        
