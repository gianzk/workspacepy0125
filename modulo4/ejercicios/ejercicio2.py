import requests
url="https://pokeapi.co/api/v2/pokemon"
response=requests.get(url)


data=response.json()
results=data['results']
for i,j in enumerate(results):
    print(i+1,j['name'])

pokemonid=int(input("ingrese el numero del pokemon "))

urlPokemon=results[pokemonid-1]["url"]

responseNew=requests.get(urlPokemon)

dataPokemon=responseNew.json()

print(f"este es el pokemon {results[pokemonid-1]['name']}",dataPokemon)