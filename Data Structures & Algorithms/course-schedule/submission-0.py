class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            adjList[crs].append(pre)

        visited = set()

        def dfs(crs):
            if crs in visited:
                return False
            if adjList[crs] == []:
                return True
            
            visited.add(crs)
            for pre in adjList[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            adjList[crs] = []
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True