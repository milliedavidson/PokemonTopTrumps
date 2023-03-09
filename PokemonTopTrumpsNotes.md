# Pokemon Top Trumps Notes

We chose to do top trumps.

Originally used a cat API, which looked like lots of fun, but we were having issues:

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

- We took it turns to try fixing the problem 
- Confirmed the list definitely needed to be numbers instead of strings
- But there were no numbers to reference in the cat API
- We couldn't figure out how to get it to pull the cat stats!

Due to a short time frame to complete the game, we replace the cats API with the Pokemon API. It worked!!!

Then we added new game play:

- A running score of player vs computer (e.g. 1-0)
- Print the computer's card stats when it prints the winner, so we can see the card they got and why they won




