class Solution(object):
    def letterCombinations(self, digits):
        t2 = ['a','b','c']
        t3 = ['d','e','f']
        t4 = ['g','h','i']
        t5 = ['j','k','l']
        t6 = ['m','n','o']
        t7 = ['p','q','r','s']
        t8 = ['t','u','v']
        t9 = ['w','x', 'y', 'z']
        
        num=[]
        for i in digits:
            num.append(i)
        print(num)
        
        listComb = []
        aux =''
        dictionary = {'2':t2, '3':t3,'4':t4, '5':t5, '6':t6, '7':t7, '8':t8, '9':t9 }
        
        if len(num)== 2:
            for i in (dictionary[num[0]]):
                for j in (dictionary[num[1]]):
                    aux += i + j
                    listComb.append(aux)
                    aux=''
                    
        if len(num)== 3:
            for i in (dictionary[num[0]]):
                for j in (dictionary[num[1]]):
                    for k in (dictionary[num[2]]):
                        aux += i + j + k
                        listComb.append(aux)
                        aux=''
        if len(num)== 4:
            for i in (dictionary[num[0]]):
                for j in (dictionary[num[1]]):
                    for k in (dictionary[num[2]]):
                        for l in (dictionary[num[3]]):
                            aux += i + j + k + l
                            listComb.append(aux)
                            aux=''
        if len(num)== 5:
            for i in (dictionary[num[0]]):
                for j in (dictionary[num[1]]):
                    for k in (dictionary[num[2]]):
                        for l in (dictionary[num[3]]):
                            for m in (dictionary[num[4]]):
                                aux += i + j + k+l+m
                                listComb.append(aux)
                                aux=''                               
        else:
            if len(num)==1:
                for i in (dictionary[num[0]]):
                    listComb.append(i)
            elif num is None:
                return str(listComb)

        return listComb  #

phone = Solution()
result = phone.letterCombinations("234567")
print(result)  # This print : 23
