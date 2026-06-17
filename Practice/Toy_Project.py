class Character:

    def __init__(self, name, hp, attack, job='모험가', shield=0):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.job = job
        self.shield = shield
        self.is_blocking = False

    def show_info(self):
        print(f'이름 : [self.job] {self.name} | HP : {self.hp} | 공격력 : {self.attack} | 방패 : {self.shield}')
    
    def attack_enemy(self, target):
        damage = self.attack
        if target.is_blocking:
            damage = damage // 2
        target.hp -= damage
        print(f'{self.name}이(가) {target.name}을 공격! {damage}피해!')
        if not target.is_alive():
            print(f"{target.name}이(가) 쓰러졌다!")

    def is_alive(self):
        return self.hp > 0

    def shield_block(self):
        if self.shield > 0:
            self.is_blocking = True
            self.shield -= 1
            print(f"{self.name}이(가) 방패를 들었다! (남은 횟수 : {self.shield})")
        else:
            print(f"{self.name}: 방패가 없어요!")

if __name__ == "__main__":
    hero = Character('아서', hp=150, attack=100, job='전사', shield=3)
    enemy = Character('드레곤', hp=200, attack=40, job='몬스터')

    hero.show_info()
    enemy.show_info()
    print("-" *40)

    hero.shield_block()
    enemy.attack_enemy(hero)
    hero.attack_enemy(enemy)
    hero.attack_enemy(enemy)

    print("-" *40)
    hero.show_info()
    enemy.show_info()
