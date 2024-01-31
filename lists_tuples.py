#lists and tuples practice 


data = [1,2,3,4,'text',[22,44,55]]

print(len(data))                    #6
print(data[1])                     #2
print(data[1:3])                   #[2,3]
data.append('text2')
print(data)                         #[1, 2, 3, 4, 'text', [22, 44, 55], 'text2']
data[0] = 'one'
print(data)                         #['one', 2, 3, 4, 'text', [22, 44, 55], 'text2']
del data[0]
print(data)                         #[2, 3, 4, 'text', [22, 44, 55], 'text2']

'''
for d in data:
    print(d)
    print(type(d))
'''

tpl = (1,2,3)
print(tpl)
tpl[0]='one'                        #ERROR - TUPLES ARE IMMUTABLE
tpl.append(4)                        #ERROR - TUPLES ARE IMMUTABLE