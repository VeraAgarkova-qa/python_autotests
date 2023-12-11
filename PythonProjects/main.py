import requests

response = requests.post(url='https://api.pokemonbattle.me:9104/pokemons',json={
"name": "generate",
"photo": "generate"
},
headers={'Content-Type': 'application/json', 'trainer_token': '7a19ce11d511658600552c6c83fa5afb'}, timeout=5)
print(response)

response = requests.put(url='https://api.pokemonbattle.me:9104/pokemons',json={
    "pokemon_id": "id_1905",
    "name": "Бульба",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
},
headers={'Content-Type': 'application/json', 'trainer_token': '7a19ce11d511658600552c6c83fa5afb'}, timeout=5)
print(response)

response = requests.post(url='https://api.pokemonbattle.me:9104/trainers/add_pokeball',json={
"pokemon_id": "1905"
},
headers={'Content-Type': 'application/json', 'trainer_token': '7a19ce11d511658600552c6c83fa5afb'}, timeout=5)
print(response)

print(f'Code:{response.status_code} - {response.reason}. Message {response.text}')
if response.status_code == 200:
  print('Ok!')
else:
  print('Bad!')

