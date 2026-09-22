class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emailMap = {} 
        par = [i for i in range(len(accounts))]
        rank = [1] * len(accounts)
        def find(x):
            if x != par[x]:
                par[x] = find(par[x])
            return par[x]

        def union(x,y):
            x1, x2 = find(x), find(y)
            if x1 == x2:
                return False
            
            if rank[x1] > rank[x2]:
                par[x2] = x1
                rank[x1] += rank[x2]
            else:
                par[x1] = x2
                rank[x2] += rank[x1]
            return True
            
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in emailMap:
                    union(i, emailMap[email])
                else:
                    emailMap[email] = i
        
        accountMap = defaultdict(list)
        for email, i in emailMap.items():
            rep = find(i)
            accountMap[rep].append(email)
        
        res = []
        for rep, emails in accountMap.items():
    
            res.append([accounts[rep][0]] + sorted(emails))
        return res
        