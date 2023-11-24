def appendstr():
    s1 = "Ault"
    s2 = "Kelly"
    
    s3 = ""
    
    s3 = s1[0] + s1[1] + s2 + s1[2] + s1[3]
    print(s3)
    
#appendstr()

def appendstr(s1,s2):
    
    s3 = ""
    
    # get middle index of s1
    mi = int(len(s1)/2)
    
    # using slicing get char upto middle index and store it into variable
    x = s1[:mi] # s1[0:mi] or s1[:mi] or s1[:mi:] start = (0 index), end = (middle index - 1)
    print(x) # Au
    
    # concanate first two char of s1 and s2 in s3
    s3 = x + s2
    print(s3)
    
    # using slicing get remaining char of s1
    x2 = s1[mi:] # start = middel index, end= len(str)-1 index
    print(x2)
    
    # add remaining char of s1 in s3
    s3 = s3 + x2
    print(s3)
    
    
    return x
  
s1 = "Ault" 
s2 = "Kelly"
appendstr(s1,s2)
   
    

    