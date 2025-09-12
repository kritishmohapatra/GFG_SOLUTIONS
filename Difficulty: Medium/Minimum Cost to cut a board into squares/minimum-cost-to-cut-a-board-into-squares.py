class Solution:
    def minCost(self, n, m, X, Y):
        # code here
        
        hor_pieces,ver_pieces = 1,1
        X.sort(reverse = True)
        Y.sort(reverse = True)
        i,j = 0,0
        tot_cost = 0
        while i<len(X) or j<len(Y):
            if i<len(X) and j<len(Y):
                max_cost = max(X[i],Y[j])
            elif i>=len(X) and j<len(Y): # in case one of the arrays is completely trversed , use the other
                max_cost = Y[j]
            else:
                max_cost = X[i]
            if i<len(X) and max_cost == X[i]:
                tot_cost += max_cost * hor_pieces
                ver_pieces += 1
                i+=1
            else:
                tot_cost += max_cost * ver_pieces
                hor_pieces += 1
                j+=1
            
        return tot_cost
        
        
