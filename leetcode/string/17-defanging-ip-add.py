def defangIPaddr(address):
        res=""

        for e in address:
            if e == ".":
                res = res + "[.]"
            else:
                res = res + e
        return res  
address = "255.100.50.0"
print(defangIPaddr(address))                
        