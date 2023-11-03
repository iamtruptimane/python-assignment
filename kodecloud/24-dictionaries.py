
def func1():
    usernames = {
        "Trupti": "trupti123",
        "sarah" : "sarah123",
        "ron": "ron123",
        "max": "max123",
    }
    print(usernames["Trupti"])
    print(usernames.keys())
    print(usernames.values())
    print(usernames.items())
    
    usernames.update({"neha": "neha123"}) # it will add given element
    print(usernames)
    
    usernames_copy = usernames.copy() # it will copy dict
    print(usernames_copy)
    
    del usernames["max"] # it will remove given element
    
    usernames.popitem()# it will remove last element
    print(usernames)
    
    usernames.clear() # it will remove all element
    
    for key in usernames.keys():
        print(key + " - " + usernames[key] )
    
#func1()

# dict: never print duplicate element
def func2():
    testdict = {
        "brand": "apple",
        "ram": "3",
        "year": 2020,
        "year": 2021 # 2020 will override by 2021 and it will get print
    }
    print(testdict)
func2()    
    