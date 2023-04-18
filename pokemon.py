class Pokemon:
    def __init__(self, name, level, type, max_health, current_health, is_ko):
        self.name = name 
        self.level = level
        self.type = type
        self.max_health = level
        self.current_health = current_health
        self.is_ko = is_ko

    def __repr__(self):
        return self.name

    def gain_health(self, health_to_gain):
        if self.current_health == self.max_health:
            return print("{0} is at max health already!".format(self.name))
        elif health_to_gain <= self.max_health - self.current_health:
            self.current_health += health_to_gain
            print("{0} now has {1} health".format(self.name, self.current_health))
            return self.current_health
        elif health_to_gain > self.max_health - self.current_health:
            self.current_health = self.max_health
            print("{0} is at max health again!".format(self.name))
            return self.current_health        

    def lose_health(self, health_to_lose):
        if self.current_health == 0:
            return print("{0} is already knocked out!".format(self.name))
        elif health_to_lose < self.current_health:
            self.current_health -= health_to_lose
            print("{0} now has {1}".format(self.name, self.current_health))
            return self.current_health
        elif health_to_lose >= self.current_health:
            self.current_health = 0
            self.is_ko = True
            print("{0} has 0 health and is knocked out!".format(self.name))
            return self.current_health 

    def revive(self, health_to_gain):
        self.is_ko = False
        if health_to_gain > self.max_health:
            self.current_health = self.max_health
            print("{0} has revived and regained full health!".format(self.name))
            return self.current_health
        else:
            self.current_health += health_to_gain
            print("{0} has revived and has {1} health!".format(self.name, self.current_health))
            return self.current_health

    def attack(self, other_pokemon):
        damage = 0
        if self.is_ko == True:
            print("Oh no! {} is knocked out and can't attack!".format(self.name))
        else:
            if self.type == other_pokemon.type:
                damage = self.level / 2
                print("{0} is attacking the same type - half damage dealt".format(self.name))
            elif ((self.type == 'Fire' or 'Ice') and (other_pokemon.type == 'Water')) or ((self.type == 'Water' or 'Electric') and (other_pokemon.type == 'Grass')) or ((self.type == 'Grass' or 'Ice') and (other_pokemon.type == 'Fire')):
                damage = self.level / 2
                print("{0} is attacking a stronger type - half damage dealt".format(self.name))
            elif ((self.type == 'Fire' or 'Ice') and (other_pokemon.type == 'Grass')) or ((self.type == 'Fire') and (other_pokemon.type == 'Ice')) or ((self.type == 'Electric' or 'Grass') and (other_pokemon.type == 'Water')) or ((self.type == 'Water') and (other_pokemon.type == 'Fire')):
                damage = self.level * 2
                print("{0} is attacking a weaker type - double damage dealt".format(self.name))
            else:
                damage = self.level
                print("{0} is attacking an equal type - normal damage dealt".format(self.name))
            return other_pokemon.lose_health(damage)

class Trainer:
    def __init__(self, name, pokemons, potions, active_pokemon):
        self.name = name 
        self.pokemons = pokemons
        self.potions = potions
        self.active_pokemon = 0

    def __repr__(self):
        return self.name

    def use_potion(self, active_pokemon, potion_value):
        print("{0} used a potion on {1}".format(self.name, self.active_pokemon))
        return self.active_pokemon.gain_health(potion_value)
    
    def attack_other_trainer(self, other_trainer):
        print("{0} is attacking {1}".format(self.name, other_trainer.name))
        their_pokemon = other_trainer.pokemons[other_trainer.active_pokemon]
        return self.pokemons[self.active_pokemon].attack(their_pokemon)

    def switch_pokemon(self, new_pokemon_num):
        old = self.pokemons[self.active_pokemon]
        new = self.pokemons[new_pokemon_num]
        print("{0} is being traded for {1}. {2} is now the currently active pokemon".format(old, new, new))
        if new.is_ko == True:
            return print("Uh-oh... {} is knocked out and can't become the active pokemon!".format(new))
        else:
            self.active_pokemon = new_pokemon_num
            return self.active_pokemon

    def add_pokemon(self, Pokemon):
        if len(self.pokemons) > 6:
            print("Sorry, no more room!")
        else:
            self.pokemons.append(Pokemon)
            return self.pokemons

Charzard = Pokemon('Charzard', 80, 'Fire', 80, 80, False)
Fairy = Pokemon('Fairy', 90, 'Electric', 90, 90, False)
Bubble = Pokemon('Bubble', 60, 'Water', 60, 60, False)

Joe = Trainer('Joe', [Charzard], 2, 0)
Abby = Trainer('Abby', [Fairy], 3, 0)


'''additional things to try/implement: 
have pokemon gain experience for battling and level up when they have enough points
create specific classes that inherit from the Pokemon class - ex. a Charmander class with all the functionality plus extra?
let pokemon evolve at a particular level
introduce other stats (speed, attack, defense) for Pokemon'''

  
