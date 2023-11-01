def func1():
    countries = ["USA", "India", "Africa"]
    print(countries)
    
    countries.append("spain") # add elemrnt at end of list
    print(countries)
    countries.insert(2, "uk") # add element at specific index
    print(countries)
#func1()

def swap_elements_1():
    countries = ["USA", "India", "Africa"]
    print(countries)
    
    temp = countries[0]
    countries[0]= countries[1]
    countries[1]= temp
    print(countries)
#swap_elements_1()

def swap_elements_2():
    countries = ["USA", "India", "Africa"]
    print(countries)
    
    countries[0], countries[1] = countries[1], countries[0]
    print(countries)
#swap_elements_2()

def sort_list():
    ages = [56,34,89,45,35]
    print(ages)
    
    ages.sort() # sort value from lowest to highest
    print(ages)
    
    alphabet = ["A", "e", "c", "b", "a"] # sort from lower alpha tp higher alpha
    print(alphabet)
    alphabet.sort()
    print(alphabet)
#sort_list()

def reverse_list():
    ages = [56,34,89,45,35]
    print(ages)
    
    ages.reverse() # reverse elements in list
    print(ages)
#reverse_list()

def insert_list():
    list_1= ["UK", "India", "Africa"]
    print(list_1)
    
    list_1.insert(1,8)
    print(list_1)
#insert_list()

def max_list():
    list_1 = ["Go", "Java", "C", "Python"]
    print(list_1)
    
    print(max(list_1))
#max_list()

def min_list():
    list_1 = ["Go", "Java", "C", "Python"]
    print(list_1)
    
    print(min(list_1))
#min_list()    

def pop_list():
    list_1 = [4,4,3,1]
    print(list_1)
    
    list_1.pop(2) # it removes element at specific index
    print(list_1)
#pop_list()

def index_list():
    list_1 = [0,1,2,3,4,5]
    print(list_1.index(4))
#index_list()

def adding_list_in_list():
    list_1 = [0,1,2,3,4,5]
    print(list_1)
    
    list_1[1]=[8,9]
    print(list_1)
adding_list_in_list()         
               
            
        
    
    