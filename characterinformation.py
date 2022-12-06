import character

def main():
    hero_name= ''
    hero_id = ''
    hero_shift = 0
    hero_pay = 0.0
    boss_name= ''
    boss_id = ''
    boss_level = 0
    boss_hp = 0.0
    boss_attack_damage = 0.0
    boss_lifespan = 0.0

    print ('Hero Data:')
    hero_name = input('Enter the hero name: ')
    hero_id = input('Enter the character ID number: ')
    hero_level = int(input('Enter the hero level: '))
    hero_loot = float(input('Enter the hero loot value: '))

    hero = character.Hero(hero_name, hero_id, hero_level, hero_loot)

    print ('')
    print ('Boss Details:')
    boss_name = input('Enter boss name: ')
    boss_id = input('Enter character ID number: ')
    boss_level = int(input('Enter boss level: '))
    boss_hp = float(input('Enter boss hp: '))
    boss_attack_damage = float(input('Enter boss attack damage: '))

    boss = character.Boss(boss_name, boss_id, boss_level, boss_hp, boss_attack_damage)
 
    print ('')
    print ('Hero Details:')
    print (f'Name: {hero.get_name()}')
    print (f'ID number: {hero.get_id_number()}')
    print (f'Level: {hero.get_level()}')
    print (f'Loot: ${hero.get_loot():,.2f}')


    print ('')
    print ('Boss Details: ')
    print (f'Name: {boss.get_name()}')
    print (f'ID number: {boss.get_id_number()}')
    print (f'Level: {boss.get_level()}')
    print (f'HP: {boss.get_hp()}')
    print (f'Attack Damage: {boss.get_attack_damage()}')
    print (f'Lifespan: {boss.get_lifespan():,.f} attacks')

if __name__ == '__main__':
 main()