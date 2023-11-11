class Character:
    def __init__(self, rings_collected, emeralds_collected, equipped_shield, sonic_dead, super_sonic):
        self.rings_collected = rings_collected
        self.emeralds_collected = emeralds_collected
        self.equipped_shield = equipped_shield
        self.sonic_dead = sonic_dead
        self.super_sonic = super_sonic

    def add_rings(self, ring_quantity):
        self.rings_collected += ring_quantity

    def equip_shield(self):
        self.equipped_shield = True

    def add_emerald(self):
        self.emeralds_collected += 1

    def take_damage(self):
        if self.equipped_shield:
            self.equipped_shield = False
        elif self.rings_collected > 0:
            self.rings_collected = 0
        else:
            self.sonic_dead = True

sonic = Character(0, 0, False, False, False)

while sonic.sonic_dead is False and (sonic.rings_collected < 50 or sonic.emeralds_collected < 7):
    entry = input()
    if entry == "aneis":
        ring_quantity = int(input())
        sonic.add_rings(ring_quantity)
        print(f'Sonic esta agora com {sonic.rings_collected} aneis! Gotta go fast!!!')
    elif entry == "escudo":
        if sonic.equipped_shield:
            print(f'Sonic ja esta equipado com uma protecao extra!!!')
        else:
            sonic.equip_shield()
            print("Sonic esta agora com uma camada a mais de protecao!!! Let's go!!!")
    elif entry == "dano":
        sonic.take_damage()
        print("Maldito robo do Eggman!!! Este sera seu fim, bigodudo!!!")
    elif entry == "esmeralda":
        if sonic.emeralds_collected < 6:
            sonic.add_emerald()
            print(f'Sonic ainda precisa encontrar mais {7 - sonic.emeralds_collected} esmeraldas!!!')
        elif sonic.emeralds_collected == 6:
            sonic.add_emerald()
            print("Sonic acabou de encontrar a esmeralda que faltava!!!")
        else:
            print("Sonic ja possui todas as esmeraldas!!!")
    if sonic.sonic_dead:
        print("Infelizmente, nosso heroi nao conseguiu correr o bastante para derrotar seu nemesis...")
    if sonic.rings_collected >= 50 and sonic.emeralds_collected >= 7:
        print("Com o poder das esmeraldas do caos, Super Sonic conseguiu deter os planos malignos do Dr. Robotinik!!!")
