class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = [[] for _ in range(numCourses)]
        indegree = [0] * (numCourses)

        for src, dst in prerequisites:
            adjList[src].append(dst)
            indegree[dst] += 1
        
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        res = []
        while queue:
            node = queue.popleft()
            res.append(node)
            for next_node in adjList[node]:
                indegree[next_node] -= 1
                if indegree[next_node] == 0:
                    queue.append(next_node)

        
        for i in indegree:
            if i != 0:
                return []
        return res[::-1]