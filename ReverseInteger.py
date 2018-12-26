class Solution(object):
    def reverse(self, Number):
        """
        :type x: int
        :rtype: int
        """
        if(Number<0):
            N=Number*(-1)
        else:
            N=Number
        num = 0
        while (N!=0):
            x= N%10
            num = num+x
            N=N/10
            num=num*10
        rev=num/10
        
        if(Number<=0):
            rev=rev*(-1)
        if (rev<=-2**31 or rev>=2**31):
            return 0
        return rev
            
