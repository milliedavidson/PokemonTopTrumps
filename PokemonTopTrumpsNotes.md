Pokemon Top Trumps Notes

We originally used a cat API but were having issues:

- Error message: "TypeError: list indices must be integers or slices, not str"
- Because this wasn't working, several other related lines threw up errors too
- We guessed the error meant we needed numbers instead of strings in the return part of the definition

 return{
        "name": cat["name"],
        "origin": cat["origin"],
        "intelligence": cat["intelligence"],
        "playfulness": cat["playfulness"],
        "life expectancy": cat["life_expectancy"]
    }

But there were no numbers to reference in the cat API so we couldn't figure out how to get it to pull the stats!

We decided to replace the cats API with the Pokemon API for sake of time. It worked.



A few of the features:

- Score of player vs computer is tracked at beginning of game and updated at the end

player_score = 0
computer_score = 0

 result = compare_stats(player_pokemon['stats'][player_stat], computer_pokemon['stats'][player_stat])
    if result == "player":
        player_score +=1
        print("\n*** You won! ***")
    elif result == "computer":
        computer_score +=1
        print("\n*** You lost! ***")
    else:
        print("\n*** It's a draw. ***")

- A random computer pokemon ID number is generated and fetched from the API

computer_pokemon_id = random.randint(1, 151)

  computer_pokemon = fetch_pokemon_data(computer_pokemon_id)
    if not computer_pokemon:
        print("Failed to fetch Pokemon data, please try again.")
        continue

- The computer's card stats are shown after it prints the winner

 print("\nThe computer randomly got {}, which has the following stats: ".format(computer_pokemon['name'].capitalize()))
    for stat, value in computer_pokemon['stats'].items():
        print("{}: {}".format(stat.capitalize(), value))


We improved readability:

- \n for a new line
- Stars ******

 print("\n**********************")
    print("Current score: ")
    print("Player Score: {} VS Computer Score: {}".format(player_score, computer_score))
    print("**********************")

- Capitalised names

print("\nThe computer randomly got {}, which has the following stats: ".format(computer_pokemon['name'].capitalize()))

