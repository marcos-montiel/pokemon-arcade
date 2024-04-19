from typing import List
import random
import sqlite3

class Pokemon:
    def __init__(self, id, name, type1, type2, hp, attack, defense, special_attack, special_defense, speed):
        self.id = id
        self.name = name        
        self.type1 = type1
        self.type2 = type2
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.special_attack = special_attack
        self.special_defense = special_defense
        self.speed = speed 
        
def pokemon_selection(options: List[Pokemon] = None) -> Pokemon:
    if options is None:
        options = get_random_pokemons(3)
    print("Select a pokemon from these:")
    print(f"1.{options[0].name.title()} 2.{options[1].name.title()} 3.{options[2].name.title()}")
    selection = input("> ")
    try:
        selection = int(selection)
        if not selection in [1, 2, 3]:
            raise ValueError
    except ValueError:
        print("Select a valid option")
        pokemon_selection(options)
    return options[selection - 1]

def get_random_pokemons(num) -> List[Pokemon]:
    pokemons = []
    for _ in range(num):
        index = random.randint(1, 151)
        pokemon = get_pokemon(index)
        pokemons.append(pokemon)
    return pokemons

def get_pokemon(index: int) -> Pokemon:
    with sqlite3.connect("pokemon_arcade/pokedex.db") as con:
        cur = con.cursor()
        res = cur.execute("SELECT * FROM pokemons WHERE id = ?", (index,))
        row = res.fetchone()
        pokemon = Pokemon(*row)
    return pokemon
