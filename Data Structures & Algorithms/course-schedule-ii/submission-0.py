class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        from collections import defaultdict

        def dfs(course):
            if course in current:
                return False

            if course in seen:
                return True 
            
            current.add(course)

            for pre in adj_lst[course]:
                if not dfs(pre):
                    return False 
            
            current.remove(course)
            seen.add(course)
            result.append(course)
            return True 

        adj_lst = defaultdict(list)
        for c, p in prerequisites:
            adj_lst[c].append(p)
        
        seen = set()
        current = set()
        result = []

        for course in range(numCourses):
            if not dfs(course):
                return []
        return result