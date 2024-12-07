import random

# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  # Store the original health for maximum limit

    def attack(self, opponent):
        opponent.health -= self.attack_power
        print(f"{self.name} attacks {opponent.name} for {self.attack_power} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, "
              f"Attack Power: {self.attack_power}")

    def heal(self):
        heal_amount = random.randint(40,70)
        self.health += heal_amount
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"{self.name} healed by {heal_amount}, "
              f"current health amount: {self.health}/{self.max_health}")

# Warrior class (inherits from Character)
class Warrior(Character): # The warrior is obessed with being strong, and uses this in battle
    def __init__(self, name, ability="Bulk Up"):
        super().__init__(name, health=140, attack_power=25)
        self.ability = ability
        
    def special_ability(self): # Increases attack and health by a fixed number
        stat_increase = int(15)
        self.attack_power += stat_increase
        self.health += stat_increase
        print(f"{self.name} used ability {self.ability}! "
              f"Attack and Health increased by {stat_increase}. "
              f"Current attack stat: {self.attack_power} "    # displays current
              f"Current health amount: {self.health}")        # stats after being changed

# Mage class (inherits from Character)
class Mage(Character): # The mage is elegant yet powerful, they use their magic in battle
    def __init__(self, name, spell="Enhance"):
        super().__init__(name, health=100, attack_power=35,)
        self.spell = spell
    
    def special_ability(self): # increases attack by a fixed number, displays new attack power
        enhance_amount = int(10)
        self.attack_power += enhance_amount
        print(f"{self.name} cast {self.spell}! Attack increased by {enhance_amount}. "
              f"Current attack stat: {self.attack_power}")

class Centaur(Character):
    def __init__(self, name, ability="Drink Potion"):
        super().__init__(name, health=110, attack_power=40)
        self.ability = ability
        
    def special_ability(self): # the centaur likes brewing potions
        attack_increase = random.randint(1,10) # sometimes the potions dont turn out well
        self.attack_power += attack_increase
        if attack_increase <= 5:   # randomizes stat increase and displays the appropriate message
            print(f"You used {self.ability}! It tasted like frogs, attack increased "
                  f"by {attack_increase}. Current attack stat {self.attack_power}")
        elif attack_increase >= 6:
            print(f"You used {self.ability}! It tasted like delicious magic, attack increased "
                  f"by {attack_increase}. Current attack stat {self.attack_power}")
    
class Beastmaster(Character): # the beastmaster has many beast friends that aid them
    def __init__(self, name, ability="Summon Beast"):
        super().__init__(name, health=100, attack_power=30)
        self.ability = ability
        
    def special_ability(self): # it will randomly pick a beast to help
        beasts = ['Dire Wolf', 'Owlbear', 'Harpy Eagle']
        random_beast = random.choice(beasts)
        if random_beast == 'Dire Wolf':  # attack increases depending on the beast
            self.attack_power += 10      # displays the appropriate message
            print(f"{self.name} used {self.ability}! A {random_beast} came to your aid! "
                  f"Attack increased by 10. Current attack stat {self.attack_power}")
        elif random_beast == "Owlbear":
            self.attack_power += 15
            print(f"{self.name} used {self.ability}! A {random_beast} came to your aid! "
                  f"Attack increased by 15. Current attack stat {self.attack_power}")
        elif random_beast == "Harpy Eagle":
            self.attack_power += 5
            print(f"{self.name} used {self.ability}! A {random_beast} came to your aid! "
                  f"Attack increased by 5. Current attack stat {self.attack_power}")

# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)
    
    # Evil Wizard's special ability: it can regenerate health
    def regenerate(self):
        self.health += 5
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")

# Function to create player character based on user input
def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Centaur")
    print("4. Beastmaster")
    
    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Centaur(name)
    elif class_choice == '4':
        return Beastmaster(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

# Battle function with user menu for actions
def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")
        
        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            player.special_ability()
        elif choice == '3':
            player.heal()
        elif choice == '4':
            player.display_stats()
        else:
            print("Invalid choice, try again.")
            continue

        # Evil Wizard's turn to attack and regenerate
        if wizard.health > 0:
            wizard.regenerate()
            wizard.attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print(f"Congradulations! The wizard {wizard.name} has been defeated by {player.name}!")

# Main function to handle the flow of the game
def main():
    # Character creation phase
    player = create_character()

    # Evil Wizard is created
    wizard = EvilWizard("The Dark Wizard")

    # Start the battle
    battle(player, wizard)

if __name__ == "__main__":
    main()