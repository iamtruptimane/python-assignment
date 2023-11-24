def createstr(str1):
    #str1 = "JhonDipPeta"
    
    # get empty string
    res = ""
    
    # get length of str
    l = len(str1)
    
    # get middel index
    mi = int(l/2)
    
    # get middle char
    mi_char = str1[mi]
    #print(mi_char)
    
    # update res string by concnating  char of middle
    
    res= res + str1[mi - 1] # char prsent at middle index - 1
    #print(res)
    
    res = res + str1[mi] # char present at middle index
    #print(res)
    
    res = res + str1[mi + 1] # char present at middle index + 1
    #print(res)
    
    return res
 
str1 = "JhonDipPeta" 
str2 = "JaSonAy"   
    
#print(createstr(str2))

# second method
def createstr(str1):
    
    # take empty res str
    res =""
    
    # get middle index
    mi = int(len(str1)/2)
    
    # use slicing to get res char
    res = str1[mi-1:mi+2] # it will start from middle index -1 and end at middle index + 1
    
    return res
str1 = "JhonDipPeta" 
str2 = "JaSonAy" 
print(createstr(str2))

  