class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for source, dest in prerequisites:
            indegree[dest] += 1
            adjList[source].append(dest)

        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)
        while q:
            course = q.popleft()
            for neighbor in adjList[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        for degree in indegree:
            if degree != 0:
                return False
        return True


        
