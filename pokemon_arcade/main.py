from pokemon import pokemon_selection

def main() -> None:
    print("Welcome to pokemon arcade!\n")
    team = []
    for _ in range(3):
        pokemon = pokemon_selection()
        team.append(pokemon)
    print(repr(team))

if __name__ == "__main__":
    main()
