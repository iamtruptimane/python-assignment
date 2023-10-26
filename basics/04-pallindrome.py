def Ifplallindrome(p):
    return p == p[::-1]

p= "poop" 
ans= Ifplallindrome(p)  

if ans:
    print("yes")
else:
    print("no")


