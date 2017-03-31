import json
import pprint

'''

  conversion table
Python          JSON
-----------------------
dict            object
list, tuple     array
str             string
int, float      number
True            true
False           false
None            null

'''

pp = pprint.PrettyPrinter(indent=4)

pythonDic1 = {
        "data1" : 2007,
        "data2" : 2008
    }

pythonDic2 = {
        'name':'Project-MAR',
        'for' :'learning',
        'data':
            {
                1 : 'message in index 1',
                2 : 'message in index 2'
            }
    }
print('python dictionary')
print(pythonDic1)
print()
print('json print')
print(json.dumps(pythonDic1, indent=4, sort_keys=True))
print('-----------------------------')

print('python dictionary')
print(pythonDic2)
print()
print('json print')
print(json.dumps(pythonDic2, indent=4, sort_keys=False))
print('-----------------------------')
print('Search for data = 1')
temp = pythonDic2['data']
print(temp[1])


