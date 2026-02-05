import bisect

class Solution:

    def smallestDiff(self,a,b,c):
        n=len(a)
        a.sort()

        b.sort()

        c.sort()

        

        i,j,k=0,0,0

        dif=10**8

        

        while i<n and j<n and k<n:

            su=a[i]+b[j]+c[k]

            mx=max(a[i],b[j],c[k])

            

            mi=min(a[i],b[j],c[k])

            

            if mi==a[i]:

                i+=1

            elif mi==b[j]:

                j+=1

            else:

                k+=1

            

            if dif>mx-mi:

                dif=mx-mi

                t1=mx

                t3=mi

                t2=su-(mx+mi)

        ans=[t1,t2,t3]

        

        return ans