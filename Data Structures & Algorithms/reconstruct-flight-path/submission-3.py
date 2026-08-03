class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adjList = { src: [] for src, dst in tickets }
        
        tickets.sort()
        for src, dst in tickets:
            adjList[src].append(dst)

        res = ["JFK"]
        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            if src not in adjList:
                return False
 
            temp = list(adjList[src])
            for i, v in enumerate(temp):
                adjList[src].pop(i)
                res.append(v)

                if dfs(v):
                    return True

                adjList[src].insert(i, v)
                res.pop()
            return False
        
        dfs("JFK")
        return res