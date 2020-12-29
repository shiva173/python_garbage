#Task 4-3

player_name = input('input player name: ')
enemy_name = input('input enemy name: ')

player = {
    'name': player_name,
    'health': 100,
    'damage': 50,
    'armor' : 1.2
}

enemy = {
    'name': enemy_name,
    'health': 200,
    'damage': 20,
    'armor' : 1.2
}

def attack(player, enemy):

    def damage_with_armor():
        damage = player['damage'] / enemy['armor']
        enemy['health'] -= damage

        print(f"{player['name']} нанес урон {enemy['name']}(у): в размере {damage} едениц")
        print(f"текущее здоровье {enemy['name']}(а) : {enemy['health']}")
    damage_with_armor()



attack(player, enemy)