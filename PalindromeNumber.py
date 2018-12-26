class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if(x<0):
            return False
        elif(0<=x<10):
            return True
        N=x
        l=0
        num=x
        y=x

        while(N>0):
            N=N//10
            l=l+1
        l=l-1

        flag=1
        while(y>0):
            f=y//(10**l)
            last=y%10
            if(f!=last):
                flag=0
                break
            y=y%(10**l)
            y=y//10
            l=l-2

        if(flag==0):
            return False
        else:
            return True
