a = {"name": "Malathi", "age": 21, "city": "Kerala"}
for key, value in a.items():
    print(f"{key}: {value}")
a["age"] = 26
print(a) 
del a["city"]
print(a)  
