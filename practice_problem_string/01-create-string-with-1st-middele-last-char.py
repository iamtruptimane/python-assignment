def createString_1():
    str1 = "james"
    
    for char in str1:
        if char == "a" or char == "e":
            continue
        else:
            print(char, end="")
        
#createString_1()    

# second method
def creatstring_2():
    str1 = "James"
    print(str1)
    
    # get a first char and store it into variable
    res = str1[0] # res = "J"
    
    #get a length of string
    l = len(str1)
    
    # get the middle index of char
    middel = int(l/2)
    
    # get the middle char and conactenate inti the first char
    res = res + str1[middel]
    
    # get the last char:
    last = str1[l-1]
    
    # conctenate last char into first and middle char
    res= res + last
    
    print(res)
creatstring_2()   
    
    
    
       
        
        