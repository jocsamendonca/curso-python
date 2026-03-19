#6.1
'''

people = {'first_name': 'jorge', 'last_name': 'mendonça', 'age': 4, 'city': 'iguatu'}

for key, value in people.items():
    print(f'{key}: {value}')
'''    
#6.7

people_0 = {'first_name': 'jorge', 'last_name': 'mendonça', 'age': 4, 'city': 'iguatu'}
people_1 = {'first_name': 'gabriel', 'last_name': 'mendonça', 'age': 2, 'city': 'iguatu'}
people_2 = {'first_name': 'nilciana', 'last_name': 'mendonça', 'age': 34, 'city': 'iguatu'}

people = [people_0, people_1, people_2]

#print(people)

for p in people:
    print(p)