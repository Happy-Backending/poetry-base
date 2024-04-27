import requests

pokemon_name = 'ekans'

r = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}')

name = r.json().get('name')
abilities = r.json().get('abilities')
unpacked_abilities = []
for ability in abilities:
    unpacked_abilities.append(ability.get('ability').get('name'))

print(f'Name: {name}')
print(f'Abilities: {", ".join(unpacked_abilities)}')

