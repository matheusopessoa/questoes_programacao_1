coordinates_list = [[],[],[],[]]
places_list = [[],[],[],[]]
list_index = []
total_km = []
possible_places = ["Praia", "Cinema", "Balada", "Shopping"]
regions = ["Norte", "Sul", "Leste", "Oeste"]
is_end = False
while not is_end:
    data = input().split(' - ')
    if data[0] == "Fim":
        is_end = True
    else:
        region, place, coordinates = data
        if region == "Norte":
            places_list[0].append(place)
            coordinates_list[0].append(coordinates.split())
        elif region == "Sul":
            places_list[1].append(place)
            coordinates_list[1].append(coordinates.split())
        elif region == "Leste":
            places_list[2].append(place)
            coordinates_list[2].append(coordinates.split())
        elif region == "Oeste":
            places_list[3].append(place)
            coordinates_list[3].append(coordinates.split())
current_place_index = 0
total_distance_traveled = 0
hideout = input().split(', ')
km_str, gasLev = input().split(' - ')
total_km.append(km_str.split(' '))
x_coordinate = int(total_km[0][0])
y_coordinate = int(total_km[0][1])
gasoline_level = int(gasLev)
print('Cidade mapeada:')
print()
current_region = 0
while current_region < 4:
    for places in places_list:
        print(f'Zona {regions[current_region]}')
        if len(places) == 0:
            print('Nenhum local mapeado nessa zona!')
        for index in range(len(places_list[current_region])):
            print(f'- {places[index]}')
        print()
        current_region += 1
is_failed = False
is_caught = False
for i in hideout:
    if hideout.index(i) == 0:
        print(f"Recebemos informações que a Barbie está no(a) {i} mais próximo(a)... Vá atrás dela!")
        print(f"Lista dos(as) {i}s mais proximos(as):")
        for c in range(len(places_list)):
            for index in range(len(places_list[c])):
                if i in places_list[c][index]:
                    total_list = []
                    current_place = places_list[c][index]
                    total_list.append(current_place)
                    total_list.append(regions[c])
                    xb_value = int(coordinates_list[c][index][0])
                    yb_value = int(coordinates_list[c][index][1])
                    total_list.append(xb_value)
                    total_list.append(yb_value)
                    distance = float(((xb_value - x_coordinate) ** 2 + (yb_value - y_coordinate) ** 2) ** (1/2))
                    total_list.insert(0, distance)
                    list_index.append(total_list)
            print_list = sorted(list_index)
        if len(list_index) == 0:
            print(f"Nenhum(a) {i} encontrado na cidade! que tipo de informação é essa!?")
            print()
        else:
            current_place_index = 0
            for p in print_list:
                current_place_index += 1
                print(f"{current_place_index}. {p[1]} ({p[2]}) - {p[0]:.2F}km")
                distance_spent = float(print_list[0][0])
                x_coordinate = print_list[0][3]
                y_coordinate = print_list[0][4]
            gasoline_level -= distance_spent
            total_distance_traveled += distance_spent
            if gasoline_level < 0:
                is_failed = True
            else:
                print(f"Os capangas chegaram a(ao) {print_list[0][1]} ({print_list[0][2]}), mas a Barbie não estava mais lá...")
                print()
    if hideout.index(i) != 0 and hideout[-1] != i:
        if gasoline_level > 0:
            print(f"Recebemos informações que a Barbie fugiu para o(a) {i} mais distante... Vá atrás dela!")
            print(f"Lista dos(as) {i}s mais distantes:")
            for c in range(len(places_list)):
                for index in range(len(places_list[c])):
                    if i in places_list[c][index]:
                        total_list = []
                        current_place = places_list[c][index]
                        total_list.append(current_place)
                        total_list.append(regions[c])
                        xb_value = int(coordinates_list[c][index][0])
                        yb_value = int(coordinates_list[c][index][1])
                        total_list.append(xb_value)
                        total_list.append(yb_value)
                        distance = float(((xb_value - x_coordinate) ** 2 + (yb_value - y_coordinate) ** 2) ** (1/2))
                        total_list.insert(0, distance)
                        list_index.append(total_list)
                print_list = sorted(list_index, reverse=True)
            if len(list_index) == 0:
                print(f"Nenhum(a) {i} encontrado na cidade! que tipo de informação é essa!?")
                print()
            else:
                current_place_index = 0
                for p in print_list:
                    current_place_index += 1
                    print(f"{current_place_index}. {p[1]} ({p[2]}) - {p[0]:.2F}km")
                    distance_spent = print_list[0][0]
                    x_coordinate = print_list[0][3]
                    y_coordinate = print_list[0][4]
                gasoline_level -= distance_spent
                total_distance_traveled += distance_spent
                if gasoline_level < 0:
                    is_failed = True
                else:
                    print(f"Os capangas chegaram a(ao) {print_list[0][1]} ({print_list[0][2]}), mas a Barbie não estava mais lá...")
                    print()
        else:
            is_failed = True
    list_index = []
    print_list = []
    if hideout[-1] == i and not is_failed:
        if gasoline_level > 0:
            print(f"Recebemos informações que a Barbie fugiu para o(a) {i} mais distante... Vá atrás dela!")
            print(f"Lista dos(as) {i}s mais distantes:")
            for c in range(len(places_list)):
                for index in range(len(places_list[c])):
                    if i in places_list[c][index]:
                        total_list = []
                        current_place = places_list[c][index]
                        total_list.append(current_place)
                        total_list.append(regions[c])
                        xb_value = int(coordinates_list[c][index][0])
                        yb_value = int(coordinates_list[c][index][1])
                        total_list.append(xb_value)
                        total_list.append(yb_value)
                        distance = float(((xb_value - x_coordinate) ** 2 + (yb_value - y_coordinate) ** 2) ** (1/2))
                        total_list.insert(0, distance)
                        list_index.append(total_list)
                print_list = sorted(list_index, reverse=True)
            if len(list_index) == 0:
                print(f"Não tem nenhum(a) {i} no mapa e acabamos a lista de lugares, não sabemos pra onde ir... A Barbie fugiu!")
            else:
                current_place_index = 0
                for p in print_list:
                    current_place_index += 1
                    print(f"{current_place_index}. {p[1]} ({p[2]}) - {p[0]:.2f}km")
                    distance_spent = print_list[0][0]
                gasoline_level -= distance_spent
                total_distance_traveled += distance_spent
                if gasoline_level < 0:
                    is_failed = True
                else:
                    is_caught = True
        else:
            is_failed
if is_caught and gasoline_level > 0:
    print(f"Finalmente, depois de {total_distance_traveled:.2f}km percorridos, os capangas capturaram a Barbie no(a) {print_list[0][1]} ({print_list[0][2]}) - Coordenadas:({print_list[0][3]}, {print_list[0][4]})")
elif gasoline_level < 0 or is_failed:
    print("Não temos combustível suficiente para continuar a perseguição, infelizmente a Barbie conseguiu fugir!")
