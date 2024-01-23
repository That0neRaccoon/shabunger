import random
import os

class Character:
    def __init__(self, name, health, attack_damage):
        self.name = name
        self.health = health
        self.attack_damage = attack_damage

    def attack(self, other):
        damage = random.randint(1, self.attack_damage)
        other.health -= damage
        print(f"{self.name} attacks {other.name} for {damage} damage!")

    def is_alive(self):
        return self.health > 0

def battle(character1, character2):
    print(f"Battle between {character1.name} and {character2.name} begins!\n")
    
    while character1.is_alive() and character2.is_alive():
        character1.attack(character2)
        character2.attack(character1)

        print(f"{character1.name}'s health: {character1.health}")
        print(f"{character2.name}'s health: {character2.health}\n")

    if character1.is_alive():
        print(f"{character1.name} wins!")
    else:
        print(f"{character2.name} wins!")

def main():
    # Example Usage:
    hero = Character("Hero", 100, 20)
    monster = Character("Monster", 80, 15)

    battle(hero, monster)

if __name__ == "__main__":
    # Git initialization and committing
    if not os.path.exists('.git'):
        os.system('git init')
        os.system('git add .')
        os.system('git commit -m "Initial commit"')

    main()
