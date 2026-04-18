class Solution:
    def isPower(self, X, Y):
        # code here
        if(X == 1):
            if(Y == 1):
                return True
            else:
                return False
        else:
            while(Y % X == 0):
                Y = Y//X
            
            if(Y == 1):
                return True
            else:
                return False