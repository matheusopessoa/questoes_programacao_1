class Fighter:
    def __init__(self, name, fighting_power, species, included):
        self.name = name
        self.fighting_power = fighting_power
        self.species = species
        self.included = included
        self.defeated_opponents = []

    def increase_power(self):
        if self.species == "Saiyajin":
            self.fighting_power += (self.fighting_power / 10)
        elif self.species == "Hibrido-Saiyajin":
            self.fighting_power += (self.fighting_power / 5)


fighter_count = 0
object_list = []
total_power = 0

while fighter_count < 8:
    entry = input().split()
    if entry[0] == "ADD":
        duplicate_fighter = False
        entry[1] = Fighter(' '.join(entry[1:-2]), int(entry[-2]), entry[-1], True)
        for element in object_list:
            if element.name == entry[1].name:
                print(f'{entry[1].name} já está no torneio e não pode ser adicionado.')
                duplicate_fighter = True
        if not duplicate_fighter:
            fighter_count += 1
            object_list.append(entry[1])
            if fighter_count == 1:
                print(f'{entry[1].name} foi o primeiro a entrar no torneio e aguarda os outros competidores.')
            else:
                if entry[1].fighting_power > average_power:
                    print(f'Adversários se preparem!! {entry[1].name} está no Torneio e é um dos maiores favoritos a conquistar.')
                else:
                    print(f"{entry[1].name} acabou de entrar no torneio, mas acho que não vai muito longe.")

    elif entry[0] == "DEL":
        removed_fighter = False
        for element in object_list:
            if element.name == entry[1]:
                object_list.remove(element)
                print(f'Infelizmente {element.name} saiu do Torneio.')
                removed_fighter = True
                fighter_count -= 1
        if not removed_fighter:
            print(f'{entry[1]} ainda não está no Torneio para ser removido.')
    total_power = 0
    for element in object_list:
        total_power += element.fighting_power
        average_power = total_power / fighter_count

object_list = sorted(object_list, key=lambda x: x.name)

first_group = object_list[0:4]
second_group = object_list[4:8]
semi_finalists_list = []
finalists = []

#QUARTAS
print()
print(f'### QUARTAS DE FINAL ###')

for i in range(0, 4):
    if first_group[i].fighting_power > second_group[i].fighting_power:
        first_group[i].increase_power()
        semi_finalists_list.append(first_group[i])
        print(f'{first_group[i].name} numa dura batalha vence {second_group[i].name}.')
        first_group[i].defeated_opponents.append(second_group[i].name)

    else:
        second_group[i].increase_power()
        semi_finalists_list.append(second_group[i])
        print(f'{second_group[i].name} numa dura batalha vence {first_group[i].name}.')
        second_group[i].defeated_opponents.append(first_group[i].name)

semi_finalists_list = sorted(semi_finalists_list, key=lambda x: x.name)
first_semi_finalists = semi_finalists_list[0:2]
second_semi_finalists = semi_finalists_list[2:4]

#SEMI
print()
print(f'### SEMI-FINAL ###')

for i in range(0, 2):
    if first_semi_finalists[i].fighting_power > second_semi_finalists[i].fighting_power:
        first_semi_finalists[i].increase_power()
        finalists.append(first_semi_finalists[i])
        print(f'{first_semi_finalists[i].name} numa dura batalha vence {second_semi_finalists[i].name}.')
        first_semi_finalists[i].defeated_opponents.append(second_semi_finalists[i].name)

    else:
        second_semi_finalists[i].increase_power()
        finalists.append(second_semi_finalists[i])
        print(f'{second_semi_finalists[i].name} numa dura batalha vence {first_semi_finalists[i].name}.')
        second_semi_finalists[i].defeated_opponents.append(first_semi_finalists[i].name)

#FINAL
print()
print(f'### FINAL ###')

if finalists[0].fighting_power > finalists[1].fighting_power:
    finalists[0].increase_power()
    finalists[0].defeated_opponents.append(finalists[1].name)
    print(f'{finalists[0].name} numa dura batalha vence {finalists[1].name}.')
    print()
    print(f'''{finalists[0].name}, venceu o Torneio do Poder passando pelos adversários {', '.join(map(str, (finalists[0].defeated_opponents)))} com um poder de luta incrível de {int(finalists[0].fighting_power)}.''')
else:
    finalists[1].increase_power()
    finalists[1].defeated_opponents.append(finalists[0].name)
    print(f'{finalists[1].name} numa dura batalha vence {finalists[0].name}.')
    print()
    print(f'''{finalists[1].name}, venceu o Torneio do Poder passando pelos adversários {', '.join(map(str, (finalists[1].defeated_opponents)))} com um poder de luta incrível de {int(finalists[1].fighting_power)}.''')
