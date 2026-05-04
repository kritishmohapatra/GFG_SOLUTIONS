class Solution:
    def sumXOR(self, arr):
        # code here
        su = 0
        for i in range(0, 32):
    
            #  Count of zeros and ones
            zc = 0
            oc = 0
             
            for j in range(0, len(arr)):
                if (arr[j] >> i) & 1:
                    oc = oc + 1
                else:
                    zc = zc + 1
            
            # Adding individual bit sum 
            su = su + oc * zc * (1 << i)
        
        return su