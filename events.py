import random
from combat import start_combat
from player import player

def random_event():
    events = ["combat", "trap", "camp"]
    weights = [4, 2, 1]
    event_type = random.choices(events, weights=weights, k=1)[0]

    if event_type == "combat":
        print("\nYou encounter a wild enemy!")
        start_combat()
    elif event_type == "trap":
        dmg = random.randint(1, 15)
        endmg = 1
        player['HP'] -= dmg
        player['Energy'] -= endmg
        print(f"\nA hidden trap! You lose {dmg} HP.")
        print(f"You lose {endmg} energy.")
        print(" Current HP: ", round(player['HP']))
    elif event_type == "camp":
        print("\nYou visited the camp")
        if player['HP'] < player['Max_HP']:
            heal = random.randint(5, player['Heal'])
            player['HP'] += heal
            player['Energy'] = player['Max_Energy']
            print("You restored: ", heal, "HP")
            print("Your energy has been restored!")
        else:
            print("You alredy have max HP")
            player['Energy'] = player['Max_Energy']
            print("Your energy has been restored!")