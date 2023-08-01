def func1():
    list_1=[10,20,30,40,50,60,70,80,90,100]
    
    print(list_1)
    
    sum=0
    for i in list_1:
        sum=sum+i
        print(f"{sum}[{sum-i}+ {i}]")
        
func1()        