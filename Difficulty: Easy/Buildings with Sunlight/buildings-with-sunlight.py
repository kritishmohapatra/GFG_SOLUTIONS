class Solution:
    def visibleBuildings(self, arr):
        # code here
        st=[]
        for i in arr:
            if len(st)>0 and st[-1]<=i:
                st.append(i)
            if len(st)==0:
                st.append(i)
            else:
                pass
        return len(st)