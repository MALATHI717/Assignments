a = [1, 2, 3, 4, 5]
for item in a:
    print(item, end=" ")  
a[0] = 100  
a.append(6) 
print(a)   
a.insert(2, 99) 
a.remove(99)
print(a)
a.pop()      
print(a) 

