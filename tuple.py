a = (1, 2, 3, 4, 5)
for item in a:
    print(item, end=" ")  
a = list(a)  
a.append(6)   
a[0] = 100     
a.remove(2)    
a = tuple(a)  
print(a)  
