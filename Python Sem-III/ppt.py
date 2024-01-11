def battle(player, monster):
    def player_attack():
        return player['attack'] + random.randint(1, 6)

    def monster_attack():
        return monster['attack'] + random.randint(1, 6)

    def calculate_damage(attacker, defender):
        damage = attacker() - defender()
        return max(damage, 0)  # Damage cannot be negative
    def h_win():
        print ("Player Wins!")
        end()
    def m_win():
        print("Monster wins!")
    def end():
        print("Escape reality & PLay games")      
    while player['health'] > 0 and monster['health'] > 0:
        player_damage = calculate_damage(player_attack, monster_attack)
        monster['health'] -= player_damage
        print(f"Player hits for {player_damage} damage. Monster's health: {monster['health']}")

        if monster['health'] <= 0:
            h_win()
            break

        monster_damage = calculate_damage(monster_attack, player_attack)
        player['health'] -= monster_damage
        print(f"Monster hits for {monster_damage} damage. Player's health: {player['health']}")

        if player['health'] <= 0:
            m_win()
            break
import random

player_stats = {'health': 100, 'attack': 20}
monster_stats = {'health': 80, 'attack': 40}

battle(player_stats, monster_stats)
