class Solution:
    def startStation(self, gas, cost):
        #  code here
        t=sum(gas)
        req=sum(cost)
        if t<req:
            return -1
        a=0
        c=0
        for i in range(len(gas)):
            c+=gas[i]-cost[i]
            if c<0:
                a=i+1
                c=0
        return a