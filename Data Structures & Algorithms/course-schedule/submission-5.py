class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = [[0] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for source, dest in prerequisites:
            adjList[source - 1].append(dest)
            indegree[dest] += 1
        
        queue = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(indegree[i])

        while queue:
            course = queue.popleft()
            for neighbor in adjList[course - 1]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        for degree in indegree:
            if degree > 0:
                return False
            
        return True

        
