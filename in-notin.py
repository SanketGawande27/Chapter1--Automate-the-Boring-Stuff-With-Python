sports = ['cricket', 'football', 'kho-kho','Table-tanis']
print('Enter a frvt sport name:')
name = input()
if name not in sports:
    print('I do not have a sports named ' + name)
else:
    print(name + ' is my sport.')
