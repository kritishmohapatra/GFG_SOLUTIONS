class Solution():
    def checkRedundancy(self, s):
        st = []
        for ch in s:
            if ch == ")":
                top = st.pop()
                flag = True  # Assume redundant until an operator is found
                
                while top != "(":
                    # Corrected the set with missing comma
                    if top in {"+", "-", "/", "*"}:
                        flag = False
                    top = st.pop()
                
                # If no operator was found between ( and ), it's redundant
                if flag:
                    return True
            else:
                st.append(ch)
        
        return False