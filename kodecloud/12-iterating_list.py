#calculate the average of the ages given in list

def average_age():
    ages = [23,45,34,56,76]
    print(ages)
    total= 0
    for i in ages:
        total = total + i
    print(f"total of ages = {total}")
    
    average = total / len(ages)
    print(f"average of ages= {average}")
average_age()

def sum_of_elements_in_list():
    values = [2,4,6,5,8,9]
    print(values)
    sum = 0
    for i in values:
        sum = sum + i
    print(f"total sum = {sum}")
sum_of_elements_in_list()

def skip_element_in_list():
    for i in "kodeKloud":
        if i == "e" : # element "e" will be skipped
            continue
        print("letter: " , i)
skip_element_in_list()

def func2():
    for x in [0,1,1,3]:
        for y in [0,2,1,2]:
            print("*")
func2()

def func3():
    list_1= [[1,2,3,2,5], [4,5,6,7], [8,9,10]]
    for i in list_1:
        if len(i)==4:
            print(i)
func3()

def func4():
    list_1 = [1,2,3,4]
    for i, j in enumerate(list_1):
        print(i,j)
func4()                    

                            
    
        