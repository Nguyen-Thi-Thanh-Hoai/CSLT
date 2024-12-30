value = [] 
items=[x for x in input("").split(',')] 
for p in items: 
    intp = int(p, 2) 
    if not intp%3:  
     value.append(p) 
print(','.join(value))