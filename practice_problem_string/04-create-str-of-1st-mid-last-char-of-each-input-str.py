def createstr(s1,s2):
    
    # get empty result str
    s3 = ""
    
    # get first char of s1 and s2 and store ti into var
    first_char = s1[0] + s2[0]
    print(first_char) # AJ
    
    # get index of middle char of s1
    mi_s1 = int(len(s1)/2)
    print(mi_s1)
   
    # get index of middle char of s2   
    mi_s2 = int(len(s2)/2)
    print(mi_s2)
    
    # get middle char of s1 and s2 and store it into var
    middle_char = s1[mi_s1] + s2[mi_s2]
    print(middle_char) # rp
    
    # get last char of s1 and s2 and store it into var
    last_char = s1[len(s1)-1] + s2[len(s2)-1]
    print(last_char) # an
    
    # add first , middle, last char of s1 and s2 in s3
    s3 = first_char + middle_char + last_char
    print(s3)
    
s1 = "America"
s2 = "Japan"
createstr(s1,s2)    
