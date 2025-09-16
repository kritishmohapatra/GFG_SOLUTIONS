class Solution:
    def decodedString(self, s):
        # code here
        st=[]
        for i in range(len(s)):
            if s[i]!="]":
                st.append(s[i])
            else:
                word=""
                while len(st)>0 and st[-1]!="[":
                    word+=st.pop()
                word=word[::-1]
                st.pop()
                k=""
                while len(st)>0 and st[-1].isdigit():
                    k+=st.pop()
                k=k[::-1]
                n=int(k)
                repeated=word*n
                st.extend(repeated)
        return "".join(st)