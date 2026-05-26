class Characher:
    EHP = 100

    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    def show_info(self):
        print(f'이름 : {self.name} | HP : {self.hp} | 공격력 : {self.attack}')
    
    def attack_enemy(self, target):
        cls.EHP -= self.attack
        print(f'{self.name}이(가) {target}을 공격! {self.attack}피해!')

    def is_alive():
        if self.hp > 0:
            return True
        else:
            print(f'{self.name}이(가)  쓰러졌다!')
            return False