# Pokemon Top Trumps
# API site - https://pokeapi.co/api/v2/pokemon/
# API key - ????

import requests
import random

# Function to fetch Pokemon data from the API
def fetch_pokemon_data(pokemon_id):
    api_url = 'https://pokeapi.co/api/v2/pokemon/{}'.format(pokemon_id)
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        stats = {}
        for stat in data['stats']:
            stat_name = stat['stat']['name']
            stat_value = stat['base_stat']
            stats[stat_name] = stat_value
        return {'name': data['name'], 'stats': stats}
    else:
        return None

# Function to compare the chosen stats and return the winner
def compare_stats(player_stat, computer_stat):
    if player_stat > computer_stat:
        return "player"
    elif player_stat < computer_stat:
        return "computer"
    else:
        return "draw"

# Begin score taking
player_score = 0
computer_score = 0

# Main game loop
while True:
    # Card randomly selected for player
    player_pokemon_id = random.randint(1, 151)

    # Fetch the player's Pokemon data from the API
    player_pokemon = fetch_pokemon_data(player_pokemon_id)
    if not player_pokemon:
        print("Failed to fetch Pokemon data, please try again.")
        continue

    # Generate a random computer Pokemon ID
    computer_pokemon_id = random.randint(1, 151)

    # Fetch the computer's Pokemon data from the API
    computer_pokemon = fetch_pokemon_data(computer_pokemon_id)
    if not computer_pokemon:
        print("Failed to fetch Pokemon data, please try again.")
        continue

    # Print the player's card stats
    print("You have {}, which has the following stats: ".format(player_pokemon['name']))
    for stat, value in player_pokemon['stats'].items():
        print("{}: {}".format(stat.capitalize(), value))


    # Compare the stats and print the result
    player_stat = input("\nChoose a stat to compare (hp, attack, defense, special-attack, special-defense, speed): ")
    if player_stat not in player_pokemon['stats']:
        print("Invalid input, please choose a valid stat.")
        continue

    result = compare_stats(player_pokemon['stats'][player_stat], computer_pokemon['stats'][player_stat])
    if result == "player":
        player_score +=1
        print("\nYou won!")
    elif result == "computer":
        computer_score +=1
        print("\nYou lost!")
    else:
        print("\nIt's a draw.")

    # Print the computer's card
    print("\nThe computer randomly got {}, which has the following stats: ".format(computer_pokemon['name']))
    for stat, value in computer_pokemon['stats'].items():
        print("{}: {}".format(stat.capitalize(), value))

    # Current score update
    print("\n**********************")
    print("Current score: ")
    print("Player Score: {} VS Computer Score: {}".format(player_score, computer_score))
    print("**********************")

    # Play again loop
    play_again = input("\nDo you want to play again? (y/n): ")
    if play_again.lower() != "y":
        break

print("\nThank you for playing!")
