from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        v = [0] * numCourses          # visited
        pv = [0] * numCourses        # path visited (for cycle)
        safe = [0] * numCourses      # safe nodes
        
        graph = [[] for i in range(numCourses)]
        
        for c, d in prerequisites:
            graph[d].append(c)
        
        res = []
        
        def dfs(node):
            v[node] = 1
            pv[node] = 1
            
            for nei in graph[node]:
                if v[nei] == 0:
                    if dfs(nei):
                        return True
                elif pv[nei] == 1:
                    return True
            
            safe[node] = 1
            res.append(node)   # store course, not safe[node]
            pv[node] = 0
            return False
        
        for i in range(numCourses):
            if v[i] == 0:
                if dfs(i):
                    return []   # cycle found
        
        return res[::-1]   # reverse to get correct order
