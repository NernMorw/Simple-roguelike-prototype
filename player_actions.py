import random
from player import player


def actions(enemy_hp, edmg, bleed, enemy_atk, can_necromancy):
        heal_cost = 1
        fire_arrow_cost = 2
        necromancy_cost = 3
        heal_magic_cost = 2
        D = 1
        rest = 1

        spawn_skeleton = False
        fire_arrow_damg = random.randint(15, 15 * player['Level'])
        heal_magic_heal = random.randint(10, 10 * player['Level'])

        valid_actions = ["attack", "strong attack", "heal", "parry", "defence", "magic", "rest", "run"]
        action = ""
        while action not in valid_actions:
            action = input("\n[Attack / Strong Attack / Heal / Parry / Defence / Magic / Rest / Run]: ").lower()
            if action not in valid_actions:
                print("Invalid action. Please choose from the list.")
        print('\n')

        if action == "attack":
            dmg = random.randint(1, player["ATK"])
            enemy_hp -= dmg
            print(f"\n\nYou deal {dmg} damage.")
        elif action == "heal":
            healed_amount = random.randint(2, player['Heal'])
            if player['Energy'] >= heal_cost:
                if bleed > 0:
                    bleed -= 1
                    player['Energy'] -= heal_cost
                    print(f"You successfully healed 1 bleed!")
                else:
                    player['HP'] += healed_amount
                    player['Energy'] -= heal_cost
                    print(f"You successfully healed for {healed_amount} HP!")
            else:
                print(f"Not enough energy to heal! (Requires {heal_cost} energy)")
        elif action == "run":
            is_succesfull = random.randint(1, 3)
            if is_succesfull != 1 and player['Energy'] >= 2:
                print("You fled the battle!")
                player['Energy'] -= 2
                return enemy_hp, edmg, bleed, True
            else:
                print("You didn't manage to escape!")
        elif action == "parry":
            parry_cost = 2
            if player['Energy'] >= parry_cost:
                enemy_hp -= round(0.5 * edmg)
                edmg = 0
                player['Energy'] -= parry_cost
                print(f"You have successfully parry enemy attack! Enemy take {round(0.5 * enemy_atk)} damage!")
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
        elif action == "rest":
            player['Energy'] += rest
            print(f"You have recovered {rest} energy!")
        elif action == "strong" or action == "strong attack":
            strong_attack_cost = 2
            if player['Energy'] >= strong_attack_cost:
                dmg = 2 * (random.randint(1, player["ATK"]))
                enemy_hp -= dmg
                player['Energy'] -= strong_attack_cost
                print(f"\n\nYou deal {dmg} damage.")
            else:
                print(f"Not enough energy for a strong attack! (Requires {strong_attack_cost} energy)")
        elif action == "magic":
            
            print("--- Magick types ---")
            print(f"Fire arrow, cost: {fire_arrow_cost} energy.")
            print(f"Necromancy, cost: {necromancy_cost} energy.")
            print(f"Heal magic, cost: {heal_magic_cost} energy.")
            print()
                
            valid_magic_actions = ["fire arrow", "necromancy", "heal magic"]
            magic_action = 1
            while magic_action not in valid_magic_actions:
                magic_action = input("").lower()
                if magic_action not in valid_magic_actions:
                    print("Invalid magic action. Please choose from the list.")
            print('\n')

            if magic_action == "fire arrow":
                if player['Energy'] >= fire_arrow_cost:
                    enemy_hp -= fire_arrow_damg
                    player['Energy'] -= fire_arrow_cost
                    print("You have successfully cast fire arrow!")
                    print(f"Enemy took {fire_arrow_damg} damage!")
                else:
                    print(f"Not enough energy for a fire arrow! (Requires {fire_arrow_cost} energy)")
            elif magic_action == "necromancy":
                if player['Energy'] >= necromancy_cost and can_necromancy:
                    player['Energy'] -= necromancy_cost
                    print("You have successfully cast necromancy!")
                    spawn_skeleton = True
                elif not can_necromancy:
                    print("You can't cast necromancy!")
                else:
                    print(f"Not enough energy for a necromancy! (Requires {necromancy_cost} energy)")
            elif magic_action == "heal magic":
                if player['Energy'] >= heal_magic_cost:
                    player['Energy'] -= heal_magic_cost
                    player['HP'] += heal_magic_heal
                    print("You have successfully cast heal magic!")
                    print(f"You healed for {heal_magic_heal} HP.")
                else:
                    print(f"Not enough energy for a heal magic! (Requires {heal_magic_cost} energy)")
            else:
                print("Invalid magic type.")
        else:
            print("Invalid action.")

        return enemy_hp, edmg, bleed, False, spawn_skeleton