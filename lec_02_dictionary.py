#Dictionary 
d = {100: 'Mongolia', 101:'Russia', 102:'Malasya'}
print(type(d))
#access
print(d[100]);
#Adding
d[103] = 'Japan'
print(d)
#Remove
d.pop(102)
print(d)
#keys
print(d.keys())

#values
print(d.values())

#Loop
for i in d.items():
    print(i)

d1 = d.copy()
print(d1)
#update
d1[100] = 'MN'
print(d)
print(d1)

