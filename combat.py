import random
from player import player
from enemies import enemy_types
from player_actions import actions


def start_combat():
    bleed = 0
    enemy_names = list(enemy_types.keys())
    chosen_enemy_name = random.choice(enemy_names)
    current_enemy = enemy_types[chosen_enemy_name]

    level_diff = player['Level'] - current_enemy['Level']
    enemy_level_up = 1.1 ** level_diff

    if current_enemy['Level'] < player['Level']:
        current_enemy['Level'] = player['Level']
        current_enemy['Max_HP'] *= enemy_level_up
        current_enemy['ATK'] *= enemy_level_up

    if "Heal" in current_enemy:
        can_heal = True
    else:
        can_heal = False

    if "Bleed_Attack" in current_enemy:
        can_bleed_attack = True
    else:
        can_bleed_attack = False

    enemy_hp = round(current_enemy['Max_HP'])
    exp_gained = current_enemy['EXP_Gain']
    is_restored_hp_time = 0

    while enemy_hp > 0 and player["HP"] > 0:
        if is_restored_hp_time > 0:
            is_restored_hp_time -= 1
        else:
            is_restored_hp = False
        if bleed > 0:
            bleed -= 1

        enemy_atk = round(current_enemy['ATK'])
        edmg = random.randint(3, round(enemy_atk))
        bleed_attack = 0.4 * edmg
        bdmg = random.randint(1, 5)

        print("\n", player['Name'])
        print("HP:       ", round(player['HP']), "/", player['Max_HP'])
        print("Energy:   ", player['Energy'], "/", player['Max_Energy'])
        print("Level     ", player['Level'])
        print("EXP:      ", player['EXP'], "/", player['Need_EXP'])
        print("\n--- A New Enemy Appears! ---")
        print("\n", chosen_enemy_name)
        print("Enemy HP:  ", round(enemy_hp))
        print("Enemy ATK: ", enemy_atk)

        enemy_hp, edmg, bleed, fled = actions(enemy_hp, edmg, bleed, enemy_atk)

        if fled:
            return

        if player['HP'] > player['Max_HP']:
            player['HP'] = player['Max_HP']

        if enemy_hp > 0:
            if can_heal == True:
                if enemy_hp < current_enemy['Max_HP'] - 2 * current_enemy['Heal'] and not is_restored_hp:
                    enemy_hp += current_enemy['Heal']
                    print(f"{chosen_enemy_name} heal {current_enemy['Heal']} HP!")
                    is_restored_hp = True
                    is_restored_hp_time = 1
                else:
                    player["HP"] -= edmg
                    print(f"\nThe enemy hits you for {edmg} damage.")
                    is_restored_hp = False
            elif can_bleed_attack:
                if bleed == 0:
                    bleed = current_enemy['Bleed_Attack']
                    player['HP'] -= bleed_attack
                    print(f"The enemy hits you with a bloody attack for {round(bleed_attack)} damage.")
                else:
                    player['HP'] -= edmg
                    player['HP'] -= bdmg
                    print(f"\nThe enemy hits you for {edmg} damage.")
                    print(f"You lost {bdmg} HP due to bleeding.")
            else:
                player["HP"] -= edmg
                print(f"\nThe enemy hits you for {edmg} damage.")
        else:
            print(f"\nYou defeated the {chosen_enemy_name}!")
            player['EXP'] += exp_gained
            print(f"You gained {exp_gained} EXP!")
        
        input()