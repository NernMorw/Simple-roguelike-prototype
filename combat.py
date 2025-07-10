import random
from player import player
from enemies import enemy_types



def start_combat():

    enemy_names = list(enemy_types.keys())
    chosen_enemy_name = random.choice(enemy_names)
    current_enemy = enemy_types[chosen_enemy_name]
    enemy_level = current_enemy['Level']
    level_diff = player['Level'] - current_enemy['Level']
    enemy_level_up = 1.1 ** level_diff
    if current_enemy['Level'] < player['Level']:
        current_enemy['Level'] = player['Level']
        current_enemy['Max_HP'] *= enemy_level_up
        current_enemy['ATK'] *= enemy_level_up

    enemy_hp = current_enemy['Max_HP']
    enemy_atk = current_enemy['ATK']

    while enemy_hp > 0 and player["HP"] > 0:

        print("\n", player['Name'])
        print("HP:       ", player['HP'], "/", player['Max_HP'])
        print("Energy:   ", player['Energy'], "/", player['Max_Energy'])
        print("Level     ", player['Level'])
        print("EXP:      ", player['EXP'], "/", player['Need_EXP'])
        print("\n--- A New Enemy Appears! ---")
        print("\n", chosen_enemy_name)
        print("Enemy HP:  ", enemy_hp)
        print("Enemy ATK: ", enemy_atk)

        action = input("\n[Attack / Heal / Run]: ").lower()
        if action == "attack":
            dmg = random.randint(5, player["ATK"])
            enemy_hp -= dmg
            print(f"You deal {dmg} damage.")
        elif action == "heal":
            healed_amount = random.randint(2, player['Heal'])
            player['HP'] += healed_amount
            print(f"You successfully healed for {healed_amount} HP!")
            if player['HP'] > player['Max_HP']:
                player['HP'] = player['Max_HP']
        elif action == "run":
            print("You fled the battle!")
            return
        
        if enemy_hp > 0:
            edmg = random.randint(3, enemy_atk)
            player["HP"] -= edmg
            print(f"The enemy hits you for {edmg} damage.")
        else:
            print(f"You defeated the {chosen_enemy_name}!")
            player['EXP'] += current_enemy['EXP_Gain']