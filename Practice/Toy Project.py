class Characher:

    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    def show_info(self):
        print(f'이름 : {self.name} | HP : {self.hp} | 공격력 : {self.attack}')
    
    def attack_enemy(self, target):
        damage = self.attack
        if target.is_blocking:
            damage = damage // 2
        target.hp -= damage
        print(f'{self.name}이(가) {target.name}을 공격! {damage}피해!')
        if target.is_alive() < 0:
            print("{target.name}이(가) 쓰러졌다!")

    def is_alive():
        if self.hp > 0:
            return True
        else:
            print(f'{self.name}이(가)  쓰러졌다!')
            return False