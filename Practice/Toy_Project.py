class Character:

    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    def show_info(self):
        print(f'이름 : {self.name} | HP : {self.hp} | 공격력 : {self.attack}')
    
    def attack_enemy(self, target):
        damage = self.attack
        # if target.is_blocking:
        #     damage = damage // 2
        target.hp -= damage
        print(f'{self.name}이(가) {target.name}을 공격! {damage}피해!')
        if not target.is_alive():
            print(f"{target.name}이(가) 쓰러졌다!")

    def is_alive(self):
        if self.hp > 0:
            return True
        else:
            print(f'{self.name}이(가)  쓰러졌다!')
            return False
        
if __name__ == "__main__":
    hero = Character('아서', hp=150,attack=30)
    enemy = Character('드레곤', hp=200, attack=40)

    hero.show_info()
    enemy.show_info()
    print("-" *40)