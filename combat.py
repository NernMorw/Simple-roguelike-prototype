import random
from player import player
from enemies import enemy_types



def start_combat():
    
    heal_cost = 1
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

    is_restored_hp = False
    if "Heal" in current_enemy:
        can_heal = True
    else:
        can_heal = False

    enemy_hp = round(current_enemy['Max_HP'])
    exp_gained = current_enemy['EXP_Gain']

    while enemy_hp > 0 and player["HP"] > 0:
        D = 1
        enemy_atk = round(current_enemy['ATK'])
        edmg = random.randint(3, round(enemy_atk))

        print("\n", player['Name'])
        print("HP:       ", round(player['HP']), "/", player['Max_HP'])
        print("Energy:   ", player['Energy'], "/", player['Max_Energy'])
        print("Level     ", player['Level'])
        print("EXP:      ", player['EXP'], "/", player['Need_EXP'])
        print("\n--- A New Enemy Appears! ---")
        print("\n", chosen_enemy_name)
        print("Enemy HP:  ", round(enemy_hp))
        print("Enemy ATK: ", enemy_atk)

        action = input("\n[Attack / Heal / Parry / Defence / Run]: ").lower()
        print('\n\n')
        if action == "attack":
            dmg = random.randint(1, player["ATK"])
            enemy_hp -= dmg
            print(f"\n\nYou deal {dmg} damage.")
        elif action == "heal":
            healed_amount = random.randint(2, player['Heal'])
            if player['Energy'] >= heal_cost:
                player['HP'] += healed_amount
                player['Energy'] -= heal_cost
                print(f"You successfully healed for {healed_amount} HP!")
            else:
                print(f"Not enough energy to heal! (Requires {heal_cost} energy)")
            if player['HP'] > player['Max_HP']:
                player['HP'] = player['Max_HP']
        elif action == "run":
            is_succesfull = random.randint(1, 3)
            if is_succesfull != 1 and player['Energy'] >= 2:
                print("You fled the battle!")
                player['Energy'] -= 2
                return
            else:
                print("You didn't manage to escape!")
        elif action == "parry":
            parry_cost = 2
            if player['Energy'] >= parry_cost:
                enemy_hp -= 0.5 * enemy_atk
                edmg = 0
                player['Energy'] -= parry_cost
                print(f"You hane succsfully parry enemy attack! Enemy take {round(0.5 * enemy_atk)} damage!")
            else:
                print(f"Not enough energy to parry! (Requires {parry_cost} energy)")
        elif action == "defence":
            defence_cost = 1
            if player['Energy'] >= defence_cost:
                D = 2
                edmg /= D
                player['Energy'] -= defence_cost
                print(f"Enemy damage reduced by {D} times")
            else:
                print(f"Not enough energy to defence! (Requires {defence_cost} energy)")
        

        if enemy_hp > 0:
            if can_heal == True:
                if enemy_hp < current_enemy['Max_HP'] - 2 * current_enemy['Heal'] and not is_restored_hp:
                    enemy_hp += current_enemy['Heal']
                    print(f"{chosen_enemy_name} heal {current_enemy['Heal']} HP!")
                    is_restored_hp = True
                else:
                    player["HP"] -= edmg
                    print(f"\nThe enemy hits you for {edmg} damage.")
                    is_restored_hp = False
            else:
                player["HP"] -= edmg
                print(f"\nThe enemy hits you for {edmg} damage.")
        else:
            print(f"\nYou defeated the {chosen_enemy_name}!")
            player['EXP'] += exp_gained
            print(f"You gained {exp_gained} EXP!")
        
        input()
