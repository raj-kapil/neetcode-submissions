class Solution:

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict

        def cycle(course, seen):
            if course in seen:
                return True 
            
            seen.add(course)

            for pre in adj_lst[course]:
                if cycle(pre, seen):
                    return True 
            adj_lst[course] = []
            seen.remove(course)
            return False

        adj_lst = defaultdict(list)

        for c, p in prerequisites:
            adj_lst[c].append(p)

        seen = set()
        for course in range(numCourses):
            if cycle(course, seen):
                return False
        return True