#states = ['NY', 'PA', 'CA']
#states = ['New York', 'Pennsylvania', 'California']
#states = ['New York', 'NY', 'Pennsylvania', 'PA', 'California', 'CA']

states = {'NY' : 'New York', 'PA' : 'Pennsylvania', 'CA' : 'California'}

print(states['NY'])

print(type(states))

print(states.get('FL', 'State not found'))
print(states.get('NY', 'State not found'))

print(states.keys())
print(states.values())

states['FL'] = 'Florida'
print(states)

user = {'name': 'Oscar', 'height': 70, 'shoe size': 10.5, 'hair': 'Brown', 'eyes': 'Brown'}

blog_post = {'title': 'Uses for dictonaries', 'body': 'bla,bla,bla'}

print(user['name'])
print(blog_post['title'])

# Dictionaries and lists can be inside of each other
animal_sounds = {
    "cat": ["meow", "purr"],
    "dog": ["woof", "bark"],
    "fox": []
}

oscar = {'name': 'Oscar', 'height': 70, 'shoe size': 10.5, 'hair': 'Brown', 'eyes': 'Brown'}
oscarII = {'name': 'OscarII', 'height': 71, 'shoe size': 10.5, 'hair': 'Brown', 'eyes': 'Brown'}
oscarIII = {'name': 'OscarIII', 'height': 72, 'shoe size': 10.5, 'hair': 'Brown', 'eyes': 'Brown'}

people = [oscar, oscarII, oscarIII]

print(people)

for person in people:
    print(person.get('height'))