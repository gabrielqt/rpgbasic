
import enum
import random
class ClassChar (enum.Enum):
    WIZARD = 'Wizard'
    ARCHER = 'Arqueiro'
    WARRIOR = 'Warrior'
class Spell(enum.Enum):
    
    FIREBALL = 1
    ICESPIKE = 2
    WATERWALL = 3
class Character:

    def __init__(self,name,classchar:ClassChar,level,hp,attack,defense,speed,magic):
        self.name = name
        self.classchar = classchar
        self.level = level
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.magic = magic
     
    @classmethod    
    def dead(cls,char):
        if char.hp <= 0:
            print(f'{char.name} is dead')
            del char
            return
    
    def list_character(self):
        print(f'''\t NAME: {self.name} \n\t CLASS: {self.classchar.name} \n\t LEVEL: {self.level} \n\t
              \033[34mATRIBUTOS:\033[m
              \n\t HEALTH: {self.hp} \n\t ATTACK: {self.attack} \n\t DEFENSE: {self.defense} \n\t SPEED: {self.speed}\n\t MAGIC: {self.magic}''')
        
class Wizard (Character):
    
    def __init__(self,name,classchar:ClassChar,level,hp,attack,defense,speed,magic):
        super().__init__(name,classchar,level,hp,attack,defense,speed,magic)
        self.magic += magic + 100
        self.speed = speed - 20
        self.attack = attack - 20
    
    
    def cast_spell(self,spell:Spell,other:Character=None):
        
        match spell:
        
            case Spell.FIREBALL:
                
                print(f'{self.name} throws a {Spell.FIREBALL.name} 🔥 against {other.name}')
                global damage
                damage = (20 * (self.level*0.2)) - other.defense
                other.hp -= damage
                print(f'Current HP of the {other.name} : {other.hp}')
                Character.dead(other)
        
            case Spell.ICESPIKE:
                print(f'{self.name} throws {Spell.ICESPIKE.name} 🍧 against {other.name}')
                damage = (15 * (self.level*0.2))  - other.defense
                other.hp -= damage
                print(f'Current HP of the {other.name} : {other.hp}')
                Character.dead(other)
                
            case Spell.WATERWALL:
                print(f'{self.name} uses the {Spell.WATERWALL.name} 🌊')
                self.defense += 50 * (self.level*0.1)
                
        if other.hp:
            return other.hp
class Warrior(Character):
    
    
    def __init__(self,name,classchar:ClassChar,level,hp,attack,defense,speed,magic=0) :
        super().__init__(name,classchar,level,hp,attack,defense,speed,magic)
        self.attack = attack + 60
        self.defense = defense + 60
        self.speed = speed - 10
        self.hp = hp + 30
        self.magic = 0
    
    def attackwsword (self,other):
        print(f'{self.name} attacks the {other.name} with own sword forged in Norway ⚔️')
        global damage
        damage = 25 * (self.level * 0.4)
        other.hp -= damage
        Character.dead(other)
        return other.hp
    
    def shield(self):
        print(f'{self.name} used the shield for self defense!🛡️')
        self.shield += 10 * (0.5 * self.level)
        
class Archer(Character):
    
    def __init__(self,name,classchar:ClassChar,level,hp,attack,defense,speed,magic=0):
        super().__init__(name,classchar,level,hp,attack,defense,speed,magic)
        self.speed = speed + 70
        self.hp = hp + 50
        self.magic = 0
        
    def shotarrow (self,other):
        print(f'{self.name} shot a arrow on {other.name} 🏹')
        global damage
        damage = 15 * (0.35) - other.defense
        other.hp -= damage
        Character.dead(other) 
        
    def specialarrow(self,other):
        global dado
        dado = random.randint(1,8) 
        if dado >= 6:
            other.hp = 0
            print(f'{self.name} hits him special attack! and kills the {other.name} 🏹✨')
            Character.dead(other)
        else:
            print(f'{self.name} wrongs the target! 🥲')
            
#testing for its all ok            
            
robben = Archer('Robben', ClassChar.ARCHER, 100,200,200,200,200)
garen = Warrior('GAREN',ClassChar.WARRIOR,95,200,150,200,30)
robben.specialarrow(garen)

ask = int(input('oi'))

