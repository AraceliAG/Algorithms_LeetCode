class Solution(object):
    def addTwoNumbers(self, l1, l2):
        resultFinally = []
        contador = 0
        
        n =len(l1)-len(l2) #3
        
        if len(l1)> len(l2):
                for i in range(n):
                    l2.append(0)
        
        for i in range (len(l1)):
            
            valueN = (l1[i] )+ contador + ( l2[i]) #19
            contador=0
            
            if valueN >=10:
                contador += 1
                valueN= valueN -10 #8
                resultFinally.append(valueN)
                
            else:
                resultFinally.append(valueN)
        if contador ==1:
            resultFinally.append(contador)
            
        return resultFinally


solution = Solution()
l1 = [5,9,3] #395 +  216 = 611 = 116
l2 = [6,1,2] 
# l1 = [2, 4, 3]  
# l2 = [5, 6, 4] 
# l1 = [9,9,9,9,9,9,9]  
# l2 = [9,9,9,9] 

result = solution.addTwoNumbers(l1, l2)

print(result)
