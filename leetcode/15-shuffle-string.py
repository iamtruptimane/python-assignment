def restoreString(s, indices):
        
        res=[]
        empty = ""
        for i in range(len(s)):
            res.append(0)
            
        print(res)

        i=0
        while(i<len(res)):
            res[indices[i]]=s[i]
            i = i+1

        print(res)

        for i in res:
            empty = empty + i
           
        print(empty)

        return empty  
    
s = "codeleet"
indices = [4,5,6,7,0,2,1,3]

print(restoreString(s,indices))    
      


