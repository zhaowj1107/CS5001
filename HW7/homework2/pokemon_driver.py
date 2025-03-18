"""
File: pokemon_driver.py
Author: Weijian Zhao(David)
Date: 2025-03-11
Class: CS_5001, Spring_2025
Description: 
homework 2:pokemon
"""
import random
from pokemon import Pokemon


def read_pokemon_from_file(filename: str) -> list[Pokemon]:
    """
    Function -- read_pokemon_from_file
    Read the information of pokemon from file
    """
    file = open(filename, "r", encoding="utf-8")
    pokemon_list = []
    next(file)  # Skip the first line (header)
    for line in file:
        line = line.strip()
        name, attack, defense, max_health = line.split("|")
        attack = int(attack)
        defense = int(defense)
        max_health = int(max_health)
        pokemon = Pokemon(name, attack, defense, max_health)
        pokemon_list.append(pokemon)
    file.close()
    return pokemon_list


def main():
    """
    The main function
    :return None
    """
    pokemon_list = read_pokemon_from_file("all_pokemon.txt")
    pokemon_list_random = pokemon_list
    random.shuffle(pokemon_list_random)
    # index = random.randint(0, len(pokemon_list) - 1)
    pokemon1 = pokemon_list_random[0]
    pokemon2 = pokemon_list_random[1]
    print(f"Welcome, {pokemon1} and {pokemon2}!\n")

    game_round = 1
    pokemon1_revive = True
    pokemon2_revive = True

    while pokemon1.is_alive() and pokemon2.is_alive() and game_round <= 10:
        print(f"Round {game_round} begins! {pokemon1} and {pokemon2}")
        if pokemon1.attempt_attack(pokemon2):
            print(f"Attack is successful! {pokemon2.name} has {pokemon2.current_health} health remaining.")
        else:
            print("Attack is blocked!")
        if pokemon2.is_alive():
            pass
        elif pokemon2_revive and random.randint(0, 1) == 1:
            pokemon2.revive()
            pokemon2_revive = False
        else:
            print("")
            print(f"{pokemon1} has won in {game_round} round!")
            return None

        if pokemon2.attempt_attack(pokemon1):
            print(f"Attack is successful! {pokemon1.name} has {pokemon1.current_health} health remaining.")
        else:
            print("Attack is blocked!")
        if pokemon1.is_alive():
            pass
        elif pokemon1_revive and random.randint(0, 1) == 1:
            pokemon1.revive()
            pokemon1_revive = False
        else:
            print("")
            print(f"{pokemon2} has won in {game_round} round!")
            return None
        game_round += 1
        print("")
    print(f"It's a tie between {pokemon1} and {pokemon2}!")


if __name__ == "__main__":
    main()
