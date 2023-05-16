import requests

while True:
    pokemon_name = input("Enter pokemon name : ")
    if pokemon_name == 'exit':
        break
    link_url = "https://pokeapi.co/api/v2/pokemon/"

    pokemon_url = link_url + pokemon_name

    req = requests.get(pokemon_url)
    if req.status_code == 200:
        pokemon_data = req.json()

        print("Name :",pokemon_data['name'])
        print("ID :",pokemon_data['id'])
        print("Weight :",pokemon_data['weight'])
        print("Height :",pokemon_data['height'])
        print("Type :",pokemon_data['types'][0]['type']['name'])

        Abilities = []
        for ability in pokemon_data['abilities']:
            Abilities.append(ability['ability']['name'])
        print("Abilities :",end=" ")
        print(*Abilities, sep = ", ")
        
        print("Move :",pokemon_data['moves'][0]['move']['name'])
        print("------------------------------")

    else :
        print("Pokemon Not found")