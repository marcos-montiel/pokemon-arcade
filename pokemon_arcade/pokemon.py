from typing import List
from dataclasses import dataclass
from typing import Optional, List
import random
import sqlite3


@dataclass
class Pokemon:
    id: int
    name: str
    type1: str
    type2: Optional[str]
    hp: int
    attack: int
    defense: int
    special_attack: int
    special_defense: int
    speed: int


def pokemon_selection() -> Pokemon:
    options = get_random_pokemons(3)
    while True:
        print("Select a pokemon from these:")
        print(
            f"1.{options[0].name.title()} 2.{options[1].name.title()} 3.{options[2].name.title()}"
        )
        user_input: str = input("> ")
        try:
            selection: int = int(user_input)
            if selection in [1, 2, 3]:
                return options[selection - 1]
            else:
                print("Select a valid options.\n")
        except ValueError:
            print("Select a valid option.\n")


def get_random_pokemons(num: int) -> List[Pokemon]:
    pokemons: List[Pokemon] = []
    for _ in range(num):
        index: int = random.randint(1, 151)
        pokemon: Pokemon = get_pokemon(index)
        pokemons.append(pokemon)
    return pokemons


def get_pokemon(index: int) -> Pokemon:
    with sqlite3.connect("pokemon_arcade/pokedex.db") as con:
        cur: sqlite3.Cursor = con.cursor()
        res: sqlite3.Cursor = cur.execute(
            "SELECT * FROM pokemons WHERE id = ?", (index,)
        )
        row = res.fetchone()
        pokemon: Pokemon = Pokemon(*row)
    return pokemon
