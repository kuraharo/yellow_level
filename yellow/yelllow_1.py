class Solution(object):
    def isHappy(self,n):
        cnt=0
        while cnt<100:
            cnt+=1
            a=0
            while(n>0):
                a=a+(n%10)**2
                n=n/10
            n=a
            if(n==1):
                return True
        return False
